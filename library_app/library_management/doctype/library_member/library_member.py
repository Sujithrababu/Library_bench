import frappe
from frappe.model.document import Document


class LibraryMember(Document):

    def validate(self):
        self.full_name = " ".join(
            filter(None, [self.first_name, self.last_name])
        )

        if self.email and "@" not in self.email:
            frappe.throw("Please enter a valid email address")

    def after_insert(self):

        full_name = self.full_name

        if not frappe.db.exists(
            "Library Card",
            {"member_name": full_name}
        ):

            card = frappe.new_doc("Library Card")

            card.card_number = f"LC-{self.name}"
            card.member_name = full_name
            card.status = "Active"

            card.insert()