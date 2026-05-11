# Online Blood Donation Management System
**Course:** Database Systems Lab
**Group Members:** Dawood Amin & Taimur Khan
**Group:** BS Computer Science — Group B

---

## Project Description
The Online Blood Donation Management System is a web-based application that allows donors to register their information and enables users to search for available donors by blood group and city. Patients or hospitals can submit blood requests through the system. An admin panel manages donors, requests, and records.

---

## Technology Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Node.js with Express.js
- **Database:** MySQL
- **Tools:** VS Code, MySQL Workbench, GitHub

---

## Database Tables
- **ADMIN** — Stores administrator login credentials
- **HOSPITAL** — Stores hospital information linked to blood requests
- **DONOR** — Stores registered donor details and availability
- **BLOODREQUEST** — Stores blood requests submitted by patients or hospitals

---

## Repository Structure

## Repository Structure

```
blood-donation-db/
│
├── README.md
├── NORMALIZATION.md
├── DATAFLOW.md
├── generate_data.py
├── insert_data.py
├── ERD/
│   └── erd_diagram.png
├── DDL/
│   └── create_tables.sql
├── DML/
│   └── validation.sql
└── CSV/
    ├── admin.csv
    ├── hospital.csv
    ├── donor.csv
    └── bloodrequest.csv
```


    ---

## Milestones
| Milestone | Description | Status |
|-----------|-------------|--------|
| Milestone 1 | ERD and Relational Schema | ✅ Done |
| Milestone 2 | Normalization (1NF to 3NF) | ✅ Done |
| Milestone 3 | Dataset and Dataflow | ✅ Done |
| Milestone 4 | DDL Scripts | ✅ Done |
| Milestone 5 | Data Population | ✅ Done |


## GitHub Repository
https://github.com/dawoodamin1/blood-donation-db
