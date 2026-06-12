import frappe

def send_overdue_reminders():

    transactions = frappe.get_all(
        "Library Transaction",
        filters={"status": "Overdue"}
    )

    frappe.logger().info(
        f"Found {len(transactions)} overdue records"
    )