import csv
import os
import random
from datetime import datetime, timedelta

def populate_csv():
    """
    Script to populate a CSV file with 1000 entries of generated data.
    """
    
    # =================================
    # COLUMN HEADINGS CONFIGURATION
    # =================================
    # Define your column headers here
    column_headers = [
        "e_id",
        "e_first_name",
        "e_last_name",
        "e_password",
        "c_id",
        "c_first_name",
        "c_last_name",
        "c_phone",
        "c_points",
        "receipt_id",
        "cost",
        "tip",
        "hour",
        "date",
    ]
    
    # =================================
    # DATA LISTS FOR EACH COLUMN
    # =================================
    # Configure the number of entries to generate
    NUM_ENTRIES = 1000
    
    # Build lists for each column (1000 entries each)
    
    # Employee IDs (1-50, cycling through)
    e_ids = [i % 50 + 1 for i in range(NUM_ENTRIES)]
    
    # Employee first names
    e_first_names = ["John", "Jane", "Mike", "Sarah", "David", "Lisa", "Chris", "Amy", "Tom", "Emma"]
    e_first_name_list = [random.choice(e_first_names) for _ in range(NUM_ENTRIES)]
    
    # Employee last names
    e_last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    e_last_name_list = [random.choice(e_last_names) for _ in range(NUM_ENTRIES)]
    
    # Employee passwords (simple generated passwords)
    e_password_list = [f"pass{random.randint(1000, 9999)}" for _ in range(NUM_ENTRIES)]
    
    # Customer IDs (1-500, cycling through)
    c_ids = [i % 500 + 1 for i in range(NUM_ENTRIES)]
    
    # Customer first names
    c_first_names = ["Alice", "Bob", "Carol", "Dan", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    c_first_name_list = [random.choice(c_first_names) for _ in range(NUM_ENTRIES)]
    
    # Customer last names
    c_last_names = ["Anderson", "Taylor", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez"]
    c_last_name_list = [random.choice(c_last_names) for _ in range(NUM_ENTRIES)]
    
    # Customer phone numbers
    c_phone_list = [f"{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}" for _ in range(NUM_ENTRIES)]
    
    # Customer points (0-1000)
    c_points_list = [random.randint(0, 1000) for _ in range(NUM_ENTRIES)]
    
    # Receipt IDs (unique sequential)
    receipt_ids = list(range(1, NUM_ENTRIES + 1))
    
    # Costs ($5.00 - $50.00)
    cost_list = [round(random.uniform(5.00, 50.00), 2) for _ in range(NUM_ENTRIES)]
    
    # Tips (0% - 25% of cost)
    tip_list = [round(cost_list[i] * random.uniform(0, 0.25), 2) for i in range(NUM_ENTRIES)]
    
    # Hours (0-23)
    hour_list = [random.randint(0, 23) for _ in range(NUM_ENTRIES)]
    
    # Dates (random dates within the last year)
    start_date = datetime.now() - timedelta(days=365)
    date_list = [(start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d") for _ in range(NUM_ENTRIES)]
    
    # CSV file configuration
    csv_filename = "data.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
    
    # Combine all lists into rows
    data_rows = []
    for i in range(NUM_ENTRIES):
        row = [
            e_ids[i],
            e_first_name_list[i],
            e_last_name_list[i],
            e_password_list[i],
            c_ids[i],
            c_first_name_list[i],
            c_last_name_list[i],
            c_phone_list[i],
            c_points_list[i],
            receipt_ids[i],
            cost_list[i],
            tip_list[i],
            hour_list[i],
            date_list[i]
        ]
        data_rows.append(row)
    
    try:
        # Create/open CSV file for writing
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write column headers
            writer.writerow(column_headers)
            
            # Write data rows
            for row in data_rows:
                writer.writerow(row)
            
            print(f"CSV file '{csv_filename}' has been created successfully!")
            print(f"File location: {csv_filepath}")
            print(f"Total rows written: {len(data_rows) + 1} (including header)")
            print(f"Generated {NUM_ENTRIES} entries with realistic data")
    
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

def read_csv():
    """
    Optional function to read and display the CSV contents.
    """
    csv_filename = "data.csv"
    
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            print(f"\nContents of {csv_filename}:")
            print("-" * 50)
            
            for row_num, row in enumerate(reader, 1):
                print(f"Row {row_num}: {row}")
                
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found. Run populate_csv() first.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

if __name__ == "__main__":
    # Run the CSV population function
    populate_csv()
    
    # Optionally read and display the contents
    # read_csv()
