console.log("LIBRARY MEMBER JS LOADED");

frappe.ui.form.on("Library Member", {
    refresh: function(frm) {
        frappe.msgprint("Library Member Custom JS Working");
    }
});