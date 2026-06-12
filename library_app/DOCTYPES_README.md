# Library App — DocTypes Summary

Short, complete reference of DocTypes, fields, links, and special flags in this app.

## DocTypes

- **Author**
  - Fields: author_name (Data, unique, reqd), country (Data), status (Select: Active/Inactive)
  - Autoname: field:author_name
  - Links: used by Book

- **Book**
  - Key fields: book_name (Data, reqd), isbn (Data, unique, reqd), author (Link → Author), category (Link → Book Category), language (Select), total_copies (Int), available_copies (Int), status (Select: Available/Out of Stock/Inactive)
  - Other fields: description, price, published_date, added_on, book_cover, pdf_copy, publisher, rating
  - Not submittable.

- **Book Category**
  - Fields: category_name (Data, unique, reqd), tree fields (is_group, parent_book_caregory, lft, rgt)
  - Autoname: field:category_name
  - Flag: is_tree (hierarchical categories)

- **Issued Book Item** (child table)
  - Fields: book (Link → Book), quantity (Int)
  - Flag: istable — used as table rows in other DocTypes (e.g., Library Membership)

- **Library Card**
  - Fields: card_number (Data, unique), member_name (Data), status (Select: Active/Expired/Blocked)
  - Created automatically from Library Member.after_insert.

- **Library Member**
  - Fields: first_name, last_name, full_name (Data, read_only, unique, auto-filled), email (Data, unique)
  - Autoname: field:email
  - Hooks: after_insert creates a Library Card for the member.
  - Not submittable.

- **Library Membership**
  - Fields: member_name (Data, unique), from_date (Date), to_date (Date), paid (Check), issued_books (Table → Issued Book Item)
  - Autoname: field:member_name
  - Flag: is_submittable (submittable DocType)

- **Library Settings**
  - Fields: loan_period (Int), max_books_allowed (Int), fine_per_day (Currency)
  - Flag: issingle (Single DocType — settings accessed via frappe.get_single("Library Settings"))

- **Library Transaction**
  - Key fields: member (Link → Library Member), member_name (fetched), book (Link → Book), book_name (fetched), issue_date, due_date, return_date (allow_on_submit), status (Select: Draft/Issued/Returned/Overdue/Cancelled, allow_on_submit), fine_amount (Currency, read_only, allow_on_submit)
  - Autoname: format:LIB-TRN-{#####}
  - Flag: is_submittable (submittable DocType)
  - Contains lifecycle logic (validate, before_submit, on_submit, on_cancel) and whitelisted helpers (return_book, mark_overdue_transactions, start_overdue_reminders).

## Link Map (concise)
- Book.author → Author
- Book.category → Book Category
- Library Transaction.member → Library Member
- Library Transaction.book → Book
- Library Membership.issued_books (table) → Issued Book Item → Book
- Library Member.after_insert → creates Library Card (member full name → Library Card.member_name)

## Flags summary
- Submittable: Library Transaction, Library Membership
- Single: Library Settings
- Child table: Issued Book Item
- Tree: Book Category

## Permissions note
- DocType JSONs currently grant permissions mainly to System Manager. Role-specific permissions and workflows are not defined in schema files.

## Usage pointers
- Settings: use frappe.get_single("Library Settings") to read settings.
- Reports and scripts should reference DocTypes by these names (e.g., tabLibrary Transaction, tabBook).

---
Generated as a concise reference for development and reports work.
