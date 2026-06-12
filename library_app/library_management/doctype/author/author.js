// Copyright (c) 2026, Sujithra and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Author", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Author", {

    onload_post_render(frm) {

        frappe.msgprint(
            "Author Form Fully Rendered"
        );

    },

    after_save(frm) {
      
        frappe.msgprint(
            "Author Saved Successfully"+ frm.doc.author_name
        );
},
    author_name(frm) {

        frm.set_value(
            "status",
            "Active"
        );

    }
});
