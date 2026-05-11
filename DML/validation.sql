-- ============================================
-- Milestone 5 — Data Population Validation
-- Online Blood Donation Management System
-- Dawood Amin & Taimur Khan
-- ============================================

USE blood_donation_db;

-- COUNT check
SELECT 'admin' AS table_name, COUNT(*) AS total_rows FROM admin
UNION
SELECT 'hospital', COUNT(*) FROM hospital
UNION
SELECT 'donor', COUNT(*) FROM donor
UNION
SELECT 'bloodrequest', COUNT(*) FROM bloodrequest;

-- NULL check
SELECT * FROM donor WHERE full_name IS NULL OR blood_group IS NULL OR city IS NULL;
SELECT * FROM bloodrequest WHERE patient_name IS NULL OR blood_group IS NULL;

-- JOIN check (foreign key integrity)
SELECT br.request_id, br.patient_name, br.blood_group, h.hospital_name
FROM bloodrequest br
JOIN hospital h ON br.hospital_id = h.hospital_id
LIMIT 10;

-- UPDATE example
UPDATE donor SET is_available = FALSE WHERE donor_id = 1;

-- DELETE example
DELETE FROM bloodrequest WHERE request_status = 'Cancelled' AND request_id = 5;