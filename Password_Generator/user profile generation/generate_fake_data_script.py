import random
import csv

def generate_fake_data():
    first_names = []
    last_names = []
    pet_names = []
    pattern = []

    with open(r'C:\Users\pc\Desktop\Hackathon\names.txt') as file:
        first_names = [line.strip() for line in file]

    with open(r'C:\Users\pc\Desktop\Hackathon\names.txt') as file:
        last_names = [line.strip() for line in file]

    with open(r'C:\Users\pc\Desktop\Hackathon\names.txt') as file:
        pet_names = [line.strip() for line in file]

    with open(r'C:\Users\pc\Desktop\Hackathon\pattern.txt') as file:
        pattern = [line.strip() for line in file]

    birth_year = random.randint(1950, 2005)
    phone_number = ''.join(str(random.randint(0, 9)) for _ in range(10))

    fake_data = {
        "First Name": random.choice(first_names),
        "Last Name": random.choice(last_names),
        "Birth Year": birth_year,
        "Pet Name": random.choice(pet_names),
        "Phone Number": phone_number,
        "Random Pattern": random.choice(pattern)
    }

    return fake_data

# Generate and save 100 fake profiles
profiles = [generate_fake_data() for _ in range(1000)]

# Field names for the CSV
fieldnames = ["First Name", "Last Name", "Birth Year", "Pet Name", "Phone Number", "Random Pattern"]

# Writing to CSV
with open(r'C:\Users\pc\Desktop\Hackathon\fake_profiles.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for profile in profiles:
        writer.writerow(profile)

print("100 Fake Profiles saved to 'fake_profiles.csv'.")
