import frappe

def member_saved(doc, method):
    frappe.msgprint(f"Hook Executed! Member {doc.full_name} was saved.")