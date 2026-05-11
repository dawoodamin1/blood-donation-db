import csv
import random
from faker import Faker

fake = Faker()

cities = ['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Kohat', 
          'Quetta', 'Multan', 'Faisalabad', 'Rawalpindi', 'Hyderabad']

blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

genders = ['Male', 'Female']

statuses = ['Pending', 'Fulfilled', 'Cancelled']

# ── Generate admin.csv ──
with open('CSV/admin.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['admin_id', 'full_name', 'email', 'password', 'phone', 'created_at'])
    for i in range(1, 6):
        writer.writerow([
            i,
            fake.name(),
            fake.unique.email(),
            'hashed_password_' + str(i),
            '03' + str(random.randint(100000000, 999999999)),
            fake.date_time_this_year()
        ])

# ── Generate hospital.csv ──
with open('CSV/hospital.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['hospital_id', 'hospital_name', 'city', 'address', 'contact_number', 'email'])
    hospital_names = [
        'DHQ Hospital', 'Combined Military Hospital', 'Lady Reading Hospital',
        'Shaukat Khanum Hospital', 'Aga Khan Hospital', 'Services Hospital',
        'Jinnah Hospital', 'PIMS Hospital', 'Holy Family Hospital', 'Hayatabad Medical Complex'
    ]
    for i in range(1, 11):
        writer.writerow([
            i,
            hospital_names[i-1],
            random.choice(cities),
            fake.address().replace('\n', ', '),
            '091' + str(random.randint(1000000, 9999999)),
            fake.company_email()
        ])

# ── Generate donor.csv ──
with open('CSV/donor.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['donor_id', 'full_name', 'age', 'gender', 'blood_group', 
                     'city', 'contact_number', 'email', 'password', 
                     'is_available', 'registered_at'])
    for i in range(1, 101):
        writer.writerow([
            i,
            fake.name(),
            random.randint(18, 50),
            random.choice(genders),
            random.choice(blood_groups),
            random.choice(cities),
            '03' + str(random.randint(100000000, 999999999)),
            fake.unique.email(),
            'hashed_password_' + str(i),
            random.choice([1, 0]),
            fake.date_time_this_year()
        ])

# ── Generate bloodrequest.csv ──
with open('CSV/bloodrequest.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['request_id', 'patient_name', 'blood_group', 'city', 
                     'contact_number', 'hospital_id', 'request_status', 'requested_at'])
    for i in range(1, 101):
        writer.writerow([
            i,
            fake.name(),
            random.choice(blood_groups),
            random.choice(cities),
            '03' + str(random.randint(100000000, 999999999)),
            random.randint(1, 10),
            random.choice(statuses),
            fake.date_time_this_year()
        ])

print("✅ All CSV files generated successfully!")
print("admin.csv     — 5 rows")
print("hospital.csv  — 10 rows")
print("donor.csv     — 100 rows")
print("bloodrequest.csv — 100 rows")