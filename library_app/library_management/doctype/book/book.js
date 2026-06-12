// frappe.ui.form.on("Book", {

//     setup(frm) {

//         console.log("Book Setup Executed");

//         frm.set_query(
//             "author",
//             function() {

//                 return {

//                     filters: {
//                         status: "Active"
//                     }

//                 };

//             }
//         );

//     }

// });
frappe.ui.form.on("Book", {

    refresh: function(frm) {

        // Intro message for new records
        if (frm.is_new()) {
            frm.set_intro(
                "Now you can create a new Book"
            );
        }

        // Check unsaved changes
        if (frm.is_dirty()) {

            frappe.msgprint(
                "You have unsaved changes"
            );

        }

        // Custom button - Book Details Dialog
        frm.add_custom_button(
            "Book Details",

            function() {

                let d = new frappe.ui.Dialog({

                    title: "Enter Book Details",

                    fields: [
                        {
                            label: "ISBN",
                            fieldname: "isbn",
                            fieldtype: "Data",
                            reqd: 1
                        },
                        {
                            label: "Published Date",
                            fieldname: "published_date",
                            fieldtype: "Date",
                            reqd: 1
                        }
                    ],

                    primary_action_label: "Update",

                    primary_action(values) {

                        // Set values in Book form
                        frm.set_value(
                            "isbn",
                            values.isbn
                        );

                        frm.set_value(
                            "published_date",
                            values.published_date
                        );

                        // Check unsaved changes
                        if (frm.is_dirty()) {
                            frappe.msgprint(
                                "Book details updated. Please save the document."
                            );
                        }

                        d.hide();
                    }

                });

                d.show();

            }
        );

        // Reports Menu -> Book Summary
        frm.add_custom_button(
            "Book Summary",

            function() {

                frappe.msgprint(
                    `
                    <b>Book Summary</b>
                    <hr>
                    Book Name: ${frm.doc.book_name || "Not Set"}
                    <br>
                    ISBN: ${frm.doc.isbn || "Not Set"}
                    <br>
                    Author: ${frm.doc.author || "Not Set"}
                    <br>
                    Published Date: ${frm.doc.published_date || "Not Set"}
                    `
                );

            },

            "Reports"
        );

    }

});