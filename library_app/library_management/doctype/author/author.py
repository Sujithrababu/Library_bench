# Copyright (c) 2026, Sujithra and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document


class Author(Document):

    def validate(self):

        books = frappe.get_all("Book")

        frappe.msgprint(
            f"Total no of Books available: {len(books)}"
        )

        if books:

            book = frappe.get_doc(
                "Book",
                books[0].name
            )

            frappe.msgprint(
                f"First Book name is : {book.book_name}"
            )

    # def after_insert(self):

    #     book = frappe.new_doc("Book")

    #     book.book_name = "Test Book"

    #     book.insert()

    #     frappe.msgprint(
    #         "Book Created"
    #     )