# Library Management System

A Frappe-based Library Management application for managing books, members, library cards, book issuing, returns, overdue tracking, fines, reports, and purchase approval workflow.

## Features Implemented

- Book management with ISBN, author, category, language, stock count, availability status, cover image, PDF copy, publisher, price, and rating.
- Author management with unique author records and active/inactive status.
- Hierarchical book category management using tree structure.
- Library member registration with auto-generated full name and email validation.
- Automatic library card creation when a new member is added.
- Library transaction flow for issuing, returning, cancelling, and tracking books.
- Automatic available-copy updates when books are issued, returned, or cancelled.
- Loan period, maximum books allowed, and fine-per-day configuration through Library Settings.
- Validation for inactive books, out-of-stock books, due dates, return dates, and member issue limits.
- Fine calculation for overdue returns.
- Daily scheduler to mark overdue transactions automatically.
- Background job trigger for overdue reminder processing.
- Email notification when a book is successfully issued.
- Submittable Library Transaction and Library Membership DocTypes.
- Book Purchase Request workflow with Librarian, Library Manager, and Purchase Manager approval stages.
- Workflow actions for sending approval, approving, rejecting, and marking books as purchased.
- Reports for issued books, available books, overdue books, library members, and member activity.
- Dashboard number cards for total books, available books, issued books, overdue books, and total members.
- Custom client scripts and web form script support for member-related workflows.

## Main DocTypes

- Author
- Book
- Book Category
- Library Member
- Library Card
- Library Membership
- Library Transaction
- Library Settings
- Issued Book Item
- Book Purchase Request

## Automation

- Daily overdue transaction check.
- Automatic book stock updates.
- Automatic library card generation.
- Issue confirmation email.
- Background overdue reminder trigger.

## Reports & Dashboard

The app includes ready-to-use reports and dashboard cards to monitor library operations such as book availability, issued books, overdue books, total books, and registered members.

## Frappe Concepts Implemented

- Custom DocTypes
- Single DocType
- Child Table DocType
- Tree DocType
- Submittable DocTypes
- Workflow
- Workflow States
- Workflow Actions
- Fixtures
- Reports
- Number Cards
- Scheduler Events
- Document Events
- Whitelisted Methods
- Background Jobs
- Client Scripts
- Web Form Script
- Email Notification

## License

MIT
