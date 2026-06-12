// Copyright (c) 2026, Sujithra and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Member", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Library Member", {

    refresh(frm) {

        frm.set_df_property(
            "email",
            "reqd",
            true
        );

        if (!frm.is_new()) {

            frm.set_df_property(
                "email",
                "read_only",
                1
            );

            // Trigger custom function
            frm.trigger("test_fun");
        }

    },

    test_fun(frm) {

        frappe.msgprint(
            "This message is from test_fun()"
        );

    }

});