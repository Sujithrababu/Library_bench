frappe.ui.form.on("Library Transaction", {
    refresh(frm) {
        if (
            frm.doc.docstatus === 1 &&
            ["Issued", "Overdue"].includes(frm.doc.status)
        ) {
            frm.add_custom_button("Check Overdue Now", () => {
                frappe.call({
                    method:
                        "library_app.library_management.doctype.library_transaction.library_transaction.mark_overdue_transactions",
                    freeze: true,
                    freeze_message: "Checking overdue transactions...",
                    callback(r) {
                        if (!r.exc) {
                            frappe.msgprint(
                                `${r.message || 0} transaction(s) marked overdue`
                            );
                            frm.reload_doc();
                        }
                    },
                });
            });

            frm.add_custom_button("Return Book", () => {
                frappe.call({
                    method:
                        "library_app.library_management.doctype.library_transaction.library_transaction.return_book",
                    args: {
                        transaction: frm.doc.name,
                    },
                    freeze: true,
                    freeze_message: "Returning book...",
                    callback(r) {
                        if (!r.exc) {
                            frappe.msgprint(
                                `Book returned. Fine Amount: ${format_currency(
                                    r.message.fine_amount
                                )}`
                            );
                            frm.reload_doc();
                        }
                    },
                });
            });

            frm.add_custom_button("Send Overdue Reminders", () => {
                frappe.call({
                    method:
                        "library_app.library_management.doctype.library_transaction.library_transaction.start_overdue_reminders",
                    freeze: true,
                    freeze_message: "Starting reminder process...",
                    callback(r) {
                        if (!r.exc) {
                            frappe.msgprint(r.message);
                        }
                    },
                });
            });
        }
    },
});