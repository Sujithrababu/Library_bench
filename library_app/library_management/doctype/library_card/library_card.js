//user defined function-need to call in refresh event
function welcome_message() {

    frappe.msgprint(
        "Welcome to Library Card"
    );

}

frappe.ui.form.on("Library Card", {
 //built in event
    refresh(frm) {
        welcome_message();

        frm.add_custom_button(
              "Activate Card",
              function() {
                     frappe.msgprint("Card Activated");
              }
              );
              
    },
 //Field event
    member_name(frm) {

        frappe.msgprint("Member Name Changed");

        frm.set_value(
            "member_name",
            frm.doc.member_name.toUpperCase()
        );

    },
 //Built in event
    validate(frm) {

        if (!frm.doc.card_number.startsWith("LC-")) {

            frappe.throw(
                "Invalid card number. Please enter a valid library card number."
            );

        }

        if (!frm.doc.member_name) {

            frappe.throw(
                "Member name is required."
            );

        }

    },
//Field event
    card_number(frm) {

        frappe.msgprint(
            "Card Number Changed"
        );

    },
//Field event 
    status(frm) {

        frappe.msgprint(
            "Status Changed"
        );

    }

});