# Normalization Document
## Online Blood Donation Management System
**Group Members:** Dawood Amin & Taimur Khan
**Course:** Database Systems Lab

---

## What is Normalization?
Normalization is the process of organizing a database to reduce redundancy and improve data integrity. We apply three normal forms: 1NF, 2NF, and 3NF.

---

## ADMIN Table
**Schema:** ADMIN( admin_id PK, full_name, email, password, phone, created_at )

### 1NF ✅
Every column contains a single atomic value. No repeating groups exist. admin_id is a unique primary key. No changes were needed.

### 2NF ✅
The primary key is a single column (admin_id). Since there is no composite key, partial dependency is impossible. No changes were needed.

### 3NF ✅
All columns (full_name, email, password, phone, created_at) depend directly on admin_id only. No non-key column determines another non-key column. No changes were needed.

---

## HOSPITAL Table
**Schema:** HOSPITAL( hospital_id PK, hospital_name, city, address, contact_number, email )

### 1NF ✅
Every column contains a single atomic value. No repeating groups exist. hospital_id is a unique primary key. No changes were needed.

### 2NF ✅
The primary key is a single column (hospital_id). Partial dependency cannot exist with a single column primary key. No changes were needed.

### 3NF ✅
All columns (hospital_name, city, address, contact_number, email) depend directly on hospital_id only. No transitive dependency exists between any non-key columns. No changes were needed.

---

## DONOR Table
**Schema:** DONOR( donor_id PK, full_name, age, gender, blood_group, city, contact_number, email, password, is_available, registered_at )

### 1NF ✅
Every column contains a single atomic value. donor_id is a unique primary key. No repeating groups or multi-valued attributes exist. No changes were needed.

### 2NF ✅
The primary key is a single column (donor_id). Since there is no composite key, partial dependency is impossible. No changes were needed.

### 3NF ✅
All columns depend directly and only on donor_id. There is no case where one non-key column determines another non-key column. No changes were needed.

---

## BLOODREQUEST Table
**Schema:** BLOODREQUEST( request_id PK, patient_name, blood_group, city, contact_number, hospital_id FK, request_status, requested_at )

### 1NF ✅
Every column contains a single atomic value. request_id is a unique primary key. No repeating groups exist. No changes were needed.

### 2NF ✅
The primary key is a single column (request_id). Partial dependency cannot exist with a single column primary key. No changes were needed.

### 3NF ✅
All columns depend directly on request_id only. hospital_id is a foreign key referencing the HOSPITAL table — this is a proper relationship, not a transitive dependency. No changes were needed.

---

## Conclusion
All four tables (ADMIN, HOSPITAL, DONOR, BLOODREQUEST) were already in Third Normal Form (3NF) in the original design. No structural changes were required. This is because each table was designed with a single column primary key, all attributes are atomic, and no non-key column depends on another non-key column.

---

## Final Schema After Normalization
ADMIN( admin_id PK, full_name, email, password, phone, created_at )

HOSPITAL( hospital_id PK, hospital_name, city, address, contact_number, email )

DONOR( donor_id PK, full_name, age, gender, blood_group, city, contact_number, email, password, is_available, registered_at )

BLOODREQUEST( request_id PK, patient_name, blood_group, city, contact_number, hospital_id FK, request_status, requested_at )