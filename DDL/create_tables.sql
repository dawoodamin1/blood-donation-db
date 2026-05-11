CREATE DATABASE blood_donation_db;
USE blood_donation_db;

CREATE TABLE admin (
    admin_id     INT PRIMARY KEY AUTO_INCREMENT,
    full_name    VARCHAR(100) NOT NULL,
    email        VARCHAR(100) UNIQUE NOT NULL,
    password     VARCHAR(255) NOT NULL,
    phone        VARCHAR(20),
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE hospital (
    hospital_id      INT PRIMARY KEY AUTO_INCREMENT,
    hospital_name    VARCHAR(150) NOT NULL,
    city             VARCHAR(100) NOT NULL,
    address          VARCHAR(255),
    contact_number   VARCHAR(20),
    email            VARCHAR(100)
);

CREATE TABLE donor (
    donor_id         INT PRIMARY KEY AUTO_INCREMENT,
    full_name        VARCHAR(100) NOT NULL,
    age              INT NOT NULL,
    gender           ENUM('Male','Female','Other') NOT NULL,
    blood_group      ENUM('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
    city             VARCHAR(100) NOT NULL,
    contact_number   VARCHAR(20) NOT NULL,
    email            VARCHAR(100) UNIQUE NOT NULL,
    password         VARCHAR(255) NOT NULL,
    is_available     BOOLEAN DEFAULT TRUE,
    registered_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bloodrequest (
    request_id       INT PRIMARY KEY AUTO_INCREMENT,
    patient_name     VARCHAR(100) NOT NULL,
    blood_group      ENUM('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
    city             VARCHAR(100) NOT NULL,
    contact_number   VARCHAR(20) NOT NULL,
    hospital_id      INT,
    request_status   ENUM('Pending','Fulfilled','Cancelled') DEFAULT 'Pending',
    requested_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id) ON DELETE SET NULL
);

-- Indexes for frequent search columns
CREATE INDEX idx_donor_blood_group ON donor(blood_group);
CREATE INDEX idx_donor_city ON donor(city);
CREATE INDEX idx_donor_available ON donor(is_available);
CREATE INDEX idx_bloodrequest_status ON bloodrequest(request_status);
CREATE INDEX idx_bloodrequest_hospital ON bloodrequest(hospital_id);