import csv
import os
import random
from datetime import datetime, timedelta

# call upload helper after creation
from upload_to_sheets import upload_csv_to_google_sheets

"""
HOW THIS WORKS: build customers and employees. Then populates lists for each column (i.e. one list that contains all of the 10000 entries for that column).
And then it puts it in the CSV.
"""
##########
# TODO
# employee ids: two employees per day. And less employees (?)
# customer ids: make more customers (around 80000)
##########



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
        # "e_first_name",
        # "e_last_name",
        # "e_password",
        "c_id",
        # "c_first_name",
        # "c_last_name",
        # "c_phone",
        # "c_points",
        "receipt_id",
        # "cost",
        "tip",
        "hour",
        "date",
    ]
    
    # =================================
    # DATA LISTS FOR EACH COLUMN
    # =================================
    # Configure the number of entries to generate
    NUM_ENTRIES = 1000000
    
    # =================================
    # CONSISTENT EMPLOYEE DATA
    # =================================
    # Create consistent employee records (ID, first name, last name, password stay together)
    employee_records = [
        (1, "John", "Smith", "pass1001"),
        (2, "Jane", "Johnson", "pass1002"),
        (3, "Mike", "Williams", "pass1003"),
        (4, "Sarah", "Brown", "pass1004"),
        (5, "David", "Jones", "pass1005"),
        (6, "Lisa", "Garcia", "pass1006"),
        (7, "Chris", "Miller", "pass1007"),
        (8, "Amy", "Davis", "pass1008"),
        (9, "Tom", "Rodriguez", "pass1009"),
        (10, "Emma", "Martinez", "pass1010"),
        (11, "Alex", "Anderson", "pass1011"),
        (12, "Maria", "Taylor", "pass1012"),
        (13, "James", "Thomas", "pass1013"),
        (14, "Jessica", "Jackson", "pass1014"),
        (15, "Robert", "White", "pass1015"),
        (16, "Ashley", "Harris", "pass1016"),
        (17, "Michael", "Martin", "pass1017"),
        (18, "Jennifer", "Thompson", "pass1018"),
        (19, "William", "Garcia", "pass1019"),
        (20, "Linda", "Martinez", "pass1020"),
        (21, "Richard", "Robinson", "pass1021"),
        (22, "Patricia", "Clark", "pass1022"),
        (23, "Charles", "Lewis", "pass1023"),
        (24, "Barbara", "Lee", "pass1024"),
        (25, "Joseph", "Walker", "pass1025"),
        (26, "Susan", "Hall", "pass1026"),
        (27, "Thomas", "Allen", "pass1027"),
        (28, "Karen", "Young", "pass1028"),
        (29, "Christopher", "Hernandez", "pass1029"),
        (30, "Nancy", "King", "pass1030"),
        (31, "Daniel", "Wright", "pass1031"),
        (32, "Betty", "Lopez", "pass1032"),
        (33, "Matthew", "Hill", "pass1033"),
        (34, "Helen", "Scott", "pass1034"),
        (35, "Anthony", "Green", "pass1035"),
        (36, "Sandra", "Adams", "pass1036"),
        (37, "Mark", "Baker", "pass1037"),
        (38, "Donna", "Gonzalez", "pass1038"),
        (39, "Donald", "Nelson", "pass1039"),
        (40, "Carol", "Carter", "pass1040"),
        (41, "Steven", "Mitchell", "pass1041"),
        (42, "Ruth", "Perez", "pass1042"),
        (43, "Paul", "Roberts", "pass1043"),
        (44, "Sharon", "Turner", "pass1044"),
        (45, "Andrew", "Phillips", "pass1045"),
        (46, "Michelle", "Campbell", "pass1046"),
        (47, "Kenneth", "Parker", "pass1047"),
        (48, "Laura", "Evans", "pass1048"),
        (49, "Joshua", "Edwards", "pass1049"),
        (50, "Sarah", "Collins", "pass1050")
    ]
    
    # =================================
    # CONSISTENT CUSTOMER DATA  
    # =================================
    # Create consistent customer records (ID, first name, last name, phone stay together)
    customer_records = [
        (1, "Alice", "Anderson", "214-555-0101"),
        (2, "Bob", "Baker", "214-555-0102"),
        (3, "Carol", "Carter", "214-555-0103"),
        (4, "Dan", "Davis", "214-555-0104"),
        (5, "Eve", "Evans", "214-555-0105"),
        (6, "Frank", "Fisher", "214-555-0106"),
        (7, "Grace", "Garcia", "214-555-0107"),
        (8, "Henry", "Harris", "214-555-0108"),
        (9, "Ivy", "Johnson", "214-555-0109"),
        (10, "Jack", "Jones", "214-555-0110"),
        # Add more customer records as needed - this is just a sample
        # You can extend this list up to 500 customers
    ]
    
    # Extend customer records to have at least 100 unique customers
    base_customers = customer_records.copy()
    while len(customer_records) < 100:
        base_id = len(customer_records) + 1
        first_names = ["Alice", "Bob", "Carol", "Dan", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
        last_names = ["Anderson", "Baker", "Carter", "Davis", "Evans", "Fisher", "Garcia", "Harris", "Johnson", "Jones"]
        customer_records.append((
            base_id,
            random.choice(first_names),
            random.choice(last_names),
            f"214-555-{base_id:04d}"
        ))
    
    # Build lists for 1000 entries by selecting from consistent records
    # Employee data (cycling through the 50 employees)
    e_ids = []
    e_first_name_list = []
    e_last_name_list = []
    e_password_list = []
    
    for i in range(NUM_ENTRIES):
        emp_record = employee_records[i % len(employee_records)]
        e_ids.append(emp_record[0])
        e_first_name_list.append(emp_record[1])
        e_last_name_list.append(emp_record[2])
        e_password_list.append(emp_record[3])
    
    # Customer data (cycling through the customers)
    c_ids = []
    c_first_name_list = []
    c_last_name_list = []
    c_phone_list = []
    
    for i in range(NUM_ENTRIES):
        cust_record = customer_records[i % len(customer_records)]
        c_ids.append(cust_record[0])
        c_first_name_list.append(cust_record[1])
        c_last_name_list.append(cust_record[2])
        c_phone_list.append(cust_record[3])
    
    # Customer points (0-1000) - this can vary per transaction
    # c_points_list = [random.randint(0, 1000) for _ in range(NUM_ENTRIES)]
    
    # Receipt IDs (unique sequential)
    receipt_ids = list(range(1, NUM_ENTRIES + 1))
    
    # Costs ($5.00 - $50.00)
    cost_list = [round(random.uniform(5.00, 50.00), 2) for _ in range(NUM_ENTRIES)]
    
    # Tips (0% - 50%, skewed toward lower values)
    # tip_list = [round(cost_list[i] * random.uniform(0, 0.25), 2) for i in range(NUM_ENTRIES)]
    tip_list = [
        round(min(random.betavariate(1, 9), 0.5), 2)
        for i in range(NUM_ENTRIES)
    ]

    # Hours (0-23 because hours are 11AM-11PM)
    hour_list = [random.randint(11, 23) for _ in range(NUM_ENTRIES)]
    
    # Dates (random dates within the last year)
    start_date = datetime.now() - timedelta(days=365)
    date_list = [(start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d") for _ in range(NUM_ENTRIES)]
    
    # CSV file configuration
    csv_filename = "receipt_data.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
    
    # Combine all lists into rows
    data_rows = []
    for i in range(NUM_ENTRIES):
        row = [
            e_ids[i],
            # e_first_name_list[i],
            # e_last_name_list[i],
            # e_password_list[i],
            c_ids[i],
            # c_first_name_list[i],
            # c_last_name_list[i],
            # c_phone_list[i],
            # c_points_list[i],
            receipt_ids[i],
            # cost_list[i],
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
            # Attempt to upload to Google Sheets if credentials/spreadsheet are configured
            try:
                creds_path = os.environ.get('GOOGLE_CREDENTIALS_PATH', 'credentials.json')
                spreadsheet_id = os.environ.get('GOOGLE_SHEETS_SPREADSHEET_ID')
                # Optional: specify the sheet/tab name (worksheet) to write to
                # Default is 'Sheet1' if not provided
                sheet_name = os.environ.get('GOOGLE_SHEETS_SHEET_NAME', 'Sheet1')
                # Call the uploader; it prints the result and returns the URL
                upload_csv_to_google_sheets(csv_filepath, spreadsheet_id=spreadsheet_id, sheet_name=sheet_name, creds_path=creds_path)
            except Exception as upload_err:
                print(f"Upload to Google Sheets skipped/failed: {upload_err}")
    
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
