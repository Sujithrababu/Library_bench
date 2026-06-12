# Copyright (c) 2026, Sujithra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_days, cint, date_diff, flt, nowdate


class LibraryTransaction(Document):
    def validate(self):
        if self.docstatus == 0:
            self.status = self.status or "Draft"
            self.fine_amount = flt(self.fine_amount)

        if self.issue_date and self.due_date and self.due_date < self.issue_date:
            frappe.throw("Due Date cannot be before Issue Date")

        if self.return_date and self.issue_date and self.return_date < self.issue_date:
            frappe.throw("Return Date cannot be before Issue Date")

    def before_submit(self):
        settings = frappe.get_single("Library Settings")

        self.issue_date = self.issue_date or nowdate()
        self.due_date = self.due_date or add_days(
            self.issue_date,
            cint(settings.loan_period)
        )
        self.status = "Issued"

        self.validate_member_limit(settings)
        self.validate_book_available()

    def on_submit(self):
        self.update_book_copies(-1)

    def on_cancel(self):
        if self.status in ("Issued", "Overdue"):
            self.update_book_copies(1)

        self.db_set("status", "Cancelled")

    def validate_book_available(self):
        book = frappe.get_doc("Book", self.book)

        if book.status == "Inactive":
            frappe.throw(f"Book {book.book_name} is inactive")

        if cint(book.available_copies) <= 0:
            frappe.throw(f"Book {book.book_name} is out of stock")

    def validate_member_limit(self, settings):
        active_transactions = frappe.db.count(
            "Library Transaction",
            {
                "member": self.member,
                "docstatus": 1,
                "status": ["in", ["Issued", "Overdue"]],
            },
        )

        if active_transactions >= cint(settings.max_books_allowed):
            frappe.throw(
                f"Member already has {active_transactions} active issued book(s)"
            )

    def update_book_copies(self, quantity_change):
        book = frappe.get_doc("Book", self.book)

        book.available_copies = (
            cint(book.available_copies)
            + quantity_change
        )

        book.save(ignore_permissions=True)


# ----------------------------
# Hook Function
# ----------------------------

def send_issue_email(doc, method):

    email = frappe.db.get_value(
        "Library Member",
        doc.member,
        "email"
    )

    if not email:
        frappe.throw(
            f"No email found for member {doc.member}"
        )

    frappe.sendmail(
        recipients=[email],
        subject="Book Issued Successfully",
        message=f"""
        Dear {doc.member_name},

        Your book has been issued successfully.

        Book: {doc.book_name}
        Transaction ID: {doc.name}
        Due Date: {doc.due_date}

        Please return the book before the due date.

        Thank you.
        """
    )

    frappe.msgprint(
        f"Email queued for {email}"
    )
# ----------------------------
# Return Book
# ----------------------------

@frappe.whitelist()
def return_book(transaction, return_date=None):

    doc = frappe.get_doc(
        "Library Transaction",
        transaction
    )

    if doc.docstatus != 1:
        frappe.throw(
            "Only submitted transactions can be returned"
        )

    if doc.status not in ("Issued", "Overdue"):
        frappe.throw(
            "This transaction is not currently issued"
        )

    return_date = return_date or nowdate()

    settings = frappe.get_single(
        "Library Settings"
    )

    overdue_days = max(
        date_diff(return_date, doc.due_date),
        0
    )

    fine_amount = (
        overdue_days
        * flt(settings.fine_per_day)
    )

    doc.db_set("return_date", return_date)
    doc.db_set("fine_amount", fine_amount)
    doc.db_set("status", "Returned")

    doc.update_book_copies(1)

    return {
        "return_date": return_date,
        "fine_amount": fine_amount,
        "overdue_days": overdue_days,
    }


# ----------------------------
# Mark Overdue
# ----------------------------

@frappe.whitelist()
def mark_overdue_transactions():

    today = nowdate()

    transactions = frappe.get_all(
        "Library Transaction",
        filters={
            "docstatus": 1,
            "status": "Issued",
            "due_date": ["<", today],
        },
        pluck="name",
    )

    for transaction in transactions:

        frappe.db.set_value(
            "Library Transaction",
            transaction,
            "status",
            "Overdue",
        )

    return len(transactions)


# ----------------------------
# Background Job Trigger
# ----------------------------

@frappe.whitelist()
def start_overdue_reminders():

    frappe.enqueue(
        "library_app.tasks.send_overdue_reminders"
    )

    return "Reminder process started"