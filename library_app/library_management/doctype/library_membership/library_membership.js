// Copyright (c) 2026, Sujithra and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Membership", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Library Membership", {

    refresh(frm) {

        // Existing functionality
        frm.toggle_display(
            "to_date",
            frm.doc.paid
        );

        // New button
        frm.add_custom_button(
            "Add Issued Book",

            function() {

                let row = frm.add_child(
                    "issued_books"
                );

                frm.refresh_field(
                    "issued_books"
                );

                frappe.msgprint(
                    "Issued Book row added"
                );

            }

        );

    },

    paid(frm) {

        frm.toggle_display(
            "to_date",
            frm.doc.paid
        );

    }

});