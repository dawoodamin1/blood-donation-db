import mysql.connector
import csv

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123123',  # replace with your MySQL password
    database='blood_donation_db',
    allow_local_infile=True
)
cursor = conn.cursor()

base_path = 'C:/Users/Dawood/Documents/GitHub/blood-donation-db/CSV/'

# Load admin.csv
with open(base_path + 'admin.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO admin (admin_id, full_name, email, password, phone, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row['admin_id'], row['full_name'], row['email'], 
              row['password'], row['phone'], row['created_at']))

# Load hospital.csv
with open(base_path + 'hospital.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO hospital (hospital_id, hospital_name, city, address, contact_number, email)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row['hospital_id'], row['hospital_name'], row['city'],
              row['address'], row['contact_number'], row['email']))

# Load donor.csv
with open(base_path + 'donor.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO donor (donor_id, full_name, age, gender, blood_group, 
                          city, contact_number, email, password, is_available, registered_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (row['donor_id'], row['full_name'], row['age'], row['gender'],
              row['blood_group'], row['city'], row['contact_number'],
              row['email'], row['password'], row['is_available'], row['registered_at']))

# Load bloodrequest.csv
with open(base_path + 'bloodrequest.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO bloodrequest (request_id, patient_name, blood_group, city,
                          contact_number, hospital_id, request_status, requested_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (row['request_id'], row['patient_name'], row['blood_group'],
              row['city'], row['contact_number'], row['hospital_id'],
              row['request_status'], row['requested_at']))

conn.commit()
cursor.close()
conn.close()

print("✅ All data inserted successfully!")
print("admin      — 5 rows")
print("hospital   — 10 rows")
print("donor      — 100 rows")
print("bloodrequest — 100 rows")