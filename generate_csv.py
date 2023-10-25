import csv
import random
import string

# Number of rows per page
rows_per_page = 1000

# Number of pages
num_pages = 200

# Function to generate random data
def generate_random_data():
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    age = random.randint(18, 80)
    city = ''.join(random.choices(string.ascii_lowercase, k=7))
    return [name, age, city]

# Generate data and write to CSV file
with open('large_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Header row

    for _ in range(num_pages * rows_per_page):
        data = generate_random_data()
        writer.writerow(data)
        
print('CSV file with {} rows generated successfully.'.format(num_pages * rows_per_page))

