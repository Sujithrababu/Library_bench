// // Copyright (c) 2026, Sujithra and contributors
// // For license information, please see license.txt


// frappe.query_reports["Member Activity Report"] = {
//     filters: [
//         {
//             fieldname: "member",
//             label: "Member",
//             fieldtype: "Link",
//             options: "Library Member"
//         }
//     ]
// }
frappe.query_reports["Member Activity Report"] = {
    filters: [
        {
            fieldname: "member",
            label: "Member",
            fieldtype: "Link",
            options: "Library Member"
        },
        {
            fieldname: "domain",
            label: "Email Domain",
            fieldtype: "Data"
        }
    ]
};