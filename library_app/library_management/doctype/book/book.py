# Copyright (c) 2026, Sujithra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Book(Document):
    def validate(self):
        if self.total_copies is None:
            self.total_copies = 0

        if self.available_copies is None:
            self.available_copies = 0

        if self.total_copies < 0:
            frappe.throw("Total Copies cannot be negative")

        if self.available_copies < 0:
            frappe.throw("Available Copies cannot be negative")

        if self.available_copies > self.total_copies:
            frappe.throw("Available Copies cannot be greater than Total Copies")

        if self.available_copies == 0:
            self.status = "Out of Stock"
        elif self.status != "Inactive":
            self.status = "Available"