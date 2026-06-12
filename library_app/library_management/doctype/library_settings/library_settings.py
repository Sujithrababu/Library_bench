# Copyright (c) 2026, Sujithra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibrarySettings(Document):
    def validate(self):
        self.loan_period = self.loan_period or 0
        self.max_books_allowed = self.max_books_allowed or 0
        self.fine_per_day = self.fine_per_day or 0

        if self.loan_period <= 0:
            frappe.throw("Loan Period must be greater than 0")

        if self.max_books_allowed <= 0:
            frappe.throw("Max Books Allowed must be greater than 0")

        if self.fine_per_day < 0:
            frappe.throw("Fine Per Day cannot be negative")
