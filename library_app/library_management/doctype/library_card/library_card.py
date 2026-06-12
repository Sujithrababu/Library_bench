# # Copyright (c) 2026, Sujithra and contributors
# # For license information, please see license.txt


import frappe
from frappe.model.document import Document


# class LibraryCard(Document):

#     # Runs before validation
#     def before_validate(self):
#         frappe.msgprint("before_validate() executed")

#     # Used for validation checks
#     def validate(self):
#         frappe.msgprint("validate() executed")

#         if not self.card_number.startswith("LC-"):
#             frappe.throw("Card Number must start with LC-")

#     # Runs before saving
#     def before_save(self):
#         frappe.msgprint("before_save() executed")

#         self.member_name = (self.member_name or "").upper()

#     # Runs only when record is created first time
#     def after_insert(self):
#         frappe.msgprint("after_insert() executed")

#     # Runs after every save/update
#     def on_update(self):
#         frappe.msgprint("on_update() executed")

#     # Runs before submit
#     def before_submit(self):
#         frappe.msgprint("before_submit() executed")

#     # Runs after submit
#     def on_submit(self):
#         frappe.msgprint("on_submit() executed")

#     # Runs before cancel
#     def before_cancel(self):
#         frappe.msgprint("before_cancel() executed")

#     # Runs after cancel
#     def on_cancel(self):
#         frappe.msgprint("on_cancel() executed")

#     # Runs before delete
#     def on_trash(self):
#         frappe.msgprint("on_trash() executed")
class LibraryCard(Document):
    def validate(self):
        if not self.card_number:
            frappe.throw("Card Number is required")

        if not self.card_number.startswith("LC-"):
            frappe.throw("Card Number must start with LC-")

        if not self.member_name:
            frappe.throw("Member Name is required")

    def before_save(self):
        self.member_name = (self.member_name or "").upper()