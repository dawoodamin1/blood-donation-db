# Dataflow Description
## Online Blood Donation Management System
**Group Members:** Dawood Amin & Taimur Khan

---

## Where Data Enters the System

Data enters the system through four points:

- **Donor Registration Form** — A donor fills in their name, age, gender, blood group, city, contact number, email, and password. This data is inserted into the `donor` table.
- **Blood Request Form** — A patient or hospital submits a blood request with patient name, required blood group, city, contact number, and hospital name. This data is inserted into the `bloodrequest` table.
- **Admin Panel** — Admin logs in using credentials stored in the `admin` table and can insert, update, or delete records in any table.
- **Hospital Records** — Admin manually adds hospital details into the `hospital` table.

---

## How Data Moves Through the System

1. Admin adds hospitals into the `hospital` table first.
2. Donors register and their data is stored in the `donor` table.
3. A patient or hospital submits a blood request. The request is stored in the `bloodrequest` table with `hospital_id` as a foreign key referencing the `hospital` table.
4. When a blood request comes in, the system queries the `donor` table to find matching donors by blood group and city.
5. Admin views all pending requests from the `bloodrequest` table and manages them from the dashboard.
6. When a donor donates, their `is_available` column in the `donor` table is updated to FALSE.
7. When a request is fulfilled, the `request_status` column in the `bloodrequest` table is updated to Fulfilled.

---

## What Comes Out

- **Search Results** — A list of available donors matching the required blood group and city, queried from the `donor` table.
- **Dashboard Statistics** — Count of available donors per blood group, queried from the `donor` table and displayed on the admin dashboard.
- **Request Reports** — List of all blood requests with their status (Pending, Fulfilled, Cancelled), joined with the `hospital` table to show hospital names.
- **Admin Reports** — Full management view of donors, requests, and hospitals.

---

## Dataflow Diagram

Donor Registration Form
↓
donor table
↓
Search Query (blood_group + city)
↓
Search Results shown to Hospital/Patient
Blood Request Form
↓
bloodrequest table ──FK──→ hospital table
↓
Admin Dashboard (manage requests)
Admin Login
↓
admin table
↓
Full control over donor, bloodrequest, hospital tables

---

## Table Dependency Order

Tables must be populated in this order to respect foreign key constraints:

1. `admin` — no dependencies
2. `hospital` — no dependencies
3. `donor` — no dependencies
4. `bloodrequest` — depends on `hospital`
