import csv
import os
import random
from typing import List
from datetime import datetime, timedelta

# call upload helper after creation
from upload_to_sheets import upload_csv_to_google_sheets

def populate_employee_records(output_filename: str = "csv_data/employee_data.csv"):
    """Create a CSV file containing the Gong Cha Employees.

    Columns: Employee ID, First Name, Last Name, Password
    """

    headers = ["EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "PASSWORD"]

    # ItemCost stored as integer cents (e.g. $5.65 => 565). Empty/unknown costs => 0
    employee_records = [
        (0, "Allen", "Basil", "Basil"),
        (1, "Gauri", "Agrawal", "Agrawal"),
        (2, "Hiya", "Sharma", "Sharma"),
        (3, "David", "Hunt", "Hunt"),
        (4, "Orlando", "Haye", "Haye"),
        (5, "Jayden", "Cox", "Cox"),
        (6, "Paul", "Taele", "Taele"),
        (7, "Darnell", "Davis", "Davis"),
        (8, "Devondre", "Jacques", "Jacques"),
        (9, "JaShaun", "Jumper", "Jumper"),
        (10, "Scooby", "Doo", "Doo"),
        (11, "Shaniqua", "Lint", "Lint"),
        (12, "Bethany", "Bright", "Bright"),
        (13, "Samantha", "Wright", "Wright"),
        (14, "Jimmy", "Olsen", "Olsen"),
        (15, "Levondre", "Light", "Light"),
        (16, "Super", "Man", "Man"),
        (17, "Bat", "Man", "Man"),
        (18, "Bruce", "Wayne", "Wayne"),
        (19, "Jason", "Todd", "Todd"),
        (20, "Dick", "Grayson", "Grayson"),
        (21, "The", "Joker", "Joker"),
        (22, "Tom", "Holland", "Holland"),
        (23, "Tim", "Drake", "Drake"),
        (24, "Quan", "Millz", "Millz"),
        (25, "Andrew", "Garfield", "Garfield"),
        (26, "Toby", "McGuire", "McGuire"),
        (27, "Damian", "Wayne", "Wayne"),
        (28, "Cassandra", "Cain", "Cain"),
        (29, "Leonardo", "DiCaprio", "DiCaprio"),
        (30, "Leonardo", "Ninja", "Ninja"),
        (31, "Raphael", "Ninja", "Ninja"),
        (32, "Donatello", "Ninja", "Ninja"),
        (33, "Michelangelo", "Ninja", "Ninja"),
        (34, "Brock", "Harrison", "Harrison"),
        (35, "Ash", "Ketchum", "Ketchum"),
        (36, "Misty", "Williams", "Williams"),
        (37, "Dwane", "Johnson", "Johnson"),
        (38, "The", "Rock", "Rock"),
        (39, "Thomas", "TheTankEngine", "TheTankEngine"),
        (40, "Caillou", "Anderson", "Anderson"),
        (41, "Nurse", "Joy", "Joy"),
        (42, "Cillian", "Murphy", "Murphy"),
        (43, "RatBasta", "Rd", "Rd"),
        (44, "John", "Cena", "Cena"),
        (45, "Ballerina", "Cappuccina", "Cappuccina"),
        (46, "Tralalero", "Tralala", "Tralala"),
        (47, "John", "Pork", "Pork"),
        (48, "Tim", "Cheese", "Cheese"),
        (49, "Bitchr", "McRae", "McRae"),
        (50, "The", "Penguin", "Penguin"),
    ]


    csv_filepath = os.path.join(os.getcwd(), output_filename)

    try:
        with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(employee_records)

    except Exception as e:
        print(f"Error writing menu CSV: {e}")
    else:
        print(f"Wrote {len(employee_records)} employees to: {csv_filepath}")


"""
HOW THIS WORKS: build customers and employees. Then populates lists for each column (i.e. one list that contains all of the 10000 entries for that column).
And then it puts it in the CSV.
"""
##########
# TODO
# tips: decimal between 0 and 0.2
# dates: last year
##########



def populate_customer_csv():
    """
    Script to populate a CSV file with 1000 entries of generated data.
    """
    
    # =================================
    # COLUMN HEADINGS CONFIGURATION
    # =================================
    # Define your column headers here
    column_headers = [
        # "RECEIPT_ID",
        # "EMPLOYEE_ID",
        # "e_first_name",
        # "e_last_name",
        # "e_password",
        "CUSTOMER_ID",
        "FIRST_NAME",
        "LAST_NAME",
        "PHONE_NUMBER",
        "REWARDS_POINTS",
       
        # "cost",
        # "TIP",
        # "ORDER_TIME",
        # "ORDER_DATE",
    ]
    
    # =================================
    # DATA LISTS FOR EACH COLUMN
    # =================================
    # Configure the number of entries to generate
    NUM_ENTRIES = 100
    
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
    c_points_list = [random.randint(0, 1000) for _ in range(NUM_ENTRIES)]
    
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
    csv_filename = "csv_data/customer_data.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
    
    # Combine all lists into rows
    data_rows = []
    for i in range(NUM_ENTRIES):
        row = [
            # receipt_ids[i],
            # e_ids[i],
            # e_first_name_list[i],
            # e_last_name_list[i],
            # e_password_list[i],
            c_ids[i],
            c_first_name_list[i],
            c_last_name_list[i],
            c_phone_list[i],
            c_points_list[i],
           
            # cost_list[i],
            # tip_list[i],
            # hour_list[i],
            # date_list[i]
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

def read_customer_csv():
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

def populate_ingredients_csv(output_filename: str = "csv_data/ingredients.csv"):
    """Create a CSV file containing the Sharetea menu items.

    Columns: IngredientID, IngredientName, Quantity, Unit
    """

    headers = ["INGREDIENT_ID", "INGREDIENT_NAME", "QUANTITY", "UNIT"]

    # ItemCost stored as integer cents (e.g. $5.65 => 565). Empty/unknown costs => 0
    ingredients = [
    (0, "Cup", 1000, "Cup"),
    (1, "Straw", 1000, "Straw"),
    (2, "Pearl", 1000, "Cups"),
    (3, "Coconut Jelly", 1000, "Cups"),
    (4, "Herbal Jelly", 1000, "Cups"),
    (5, "Ai-Yu Jelly", 1000, "Cups"),
    (6, "White Pearl", 1000, "Cups"),
    (7, "Mango Pulp Syrup", 1000, "Cups"),
    (8, "Lychee Syrup", 1000, "Cups"),
    (9, "Strawberry", 1000, "Cups"),
    (10, "Taro", 1000, "Cups"),
    (11, "Black Tea", 1000, "Cups"),
    (12, "Water", 10000, "Cups"),
    (13, "Wintermelon Syrup", 1000, "Pumps"),
    (14, "Wintermelon Honey", 1000, "Pumps"),
    (15, "Creamer Powder", 1000, "Pumps"),
    (16, "High Fructose Syrup", 1000, "Pumps"),
    (17, "Green Tea", 1000, "Cups"),
    (18, "Strawberry Pulp Syrup", 1000, "Pumps"),
    (19, "Oolong Tea", 1000, "Cups"),
    (20, "Brown Sugar", 1000, "Tbsp"),
    (21, "Caramel Syrup", 1000, "Pumps"),
    (22, "Coffee", 1000, "Cups"),
    (23, "Early Grey Tea", 1000, "Cups"),
    (24, "Whole Milk", 1000, "Cups"),
    (25, "Heavy Whipping cream", 1000, "Cups"),
    (26, "Matcha Tea Powder", 1000, "Tbsp"),
    (27, "Butter", 1000, "Tbsp"),
    (28, "Sweetend Condensed Milk", 1000, "Cups"),
    (29, "Chai Tea Powder", 1000, "Tbsp"),
    ]


    csv_filepath = os.path.join(os.getcwd(), output_filename)

    try:
        with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(ingredients)

    except Exception as e:
        print(f"Error writing menu CSV: {e}")
    else:
        print(f"Wrote {len(ingredients)} menu items to: {csv_filepath}")

def populate_sharetea_menu(output_filename: str = "csv_data/items.csv"):
    """Create a CSV file containing the Sharetea menu items.

    Columns: Item ID, Item Name, Item Category, Item Cost, Ingredients
    """

    headers = ["ITEM_ID", "ITEM_NAME", "CATEGORY", "PRICE"]
    
    menu_records = [
        (0, "Wintermelon Milk Tea", "Milk Tea", 5.75),
        (1, "Strawbery Milk Tea", "Milk Tea", 5.75),
        (2, "Milk Black Tea", "Milk Tea", 5.75),
        (3, "Oolong Tea", "Milk Tea", 5.75),
        (4, "Pearl Milk Tea", "Milk Tea", 5.75),
        (5, "Caramel Milk Tea", "Milk Tea", 5.50),
        (6, "Milk Coffee", "Coffee", 5.50),
        (7, "Coffee Milk Tea", "Coffee", 5.50),
        (8, "Milk Foam Black Coffee", "Coffee", 6.00),
        (9, "Pearl", "Toppings", 0.75),
        (10, "Coconut Jelly", "Toppings", 0.75),
        (11, "Herbal Jelly", "Toppings", 0.75),
        (12, "Ai-Yu Jelly", "Toppings", 0.75),
        (13, "White Pearl", "Toppings", 1.00),
        (14, "Matcha Tea Latte", "Tea Latte", 5.75),
        (15, "Strawberry Matcha Latte", "Tea Latte", 6.50),
        (16, "Thai Tea Latte", "Tea Latte", 6.25),
        (17, "Lychee", "Slush Series", 6.75),
        (18, "Taro Milk", "Slush Series", 6.75),
        (19, "Mango Milk", "Slush Series", 6.75),
        (20, "Strawberry Milk", "Slush Series", 6.75),
    ]

    csv_filepath = os.path.join(os.getcwd(), output_filename)

    try:
        with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for item in menu_records:
                item_id, name, category, cost = item
                writer.writerow([item_id, name, category, float(cost)])

    except Exception as e:
        print(f"Error writing menu CSV: {e}")
    else:
        print(f"Wrote {len(menu_records)} menu items to: {csv_filepath}")

def parse_int(env_name: str, default: int) -> int:
    val = os.environ.get(env_name)
    if val is None:
        return default
    try:
        return int(val)
    except ValueError:
        return default


def parse_menu_items(env_name: str, default_count: int) -> List[int]:
    val = os.environ.get(env_name)
    if not val:
        return list(range(1, default_count + 1))
    # allow comma-separated list or a single integer meaning 1..N
    if ',' in val:
        parts = [p.strip() for p in val.split(',') if p.strip()]
        try:
            return [int(p) for p in parts]
        except ValueError:
            return list(range(1, default_count + 1))
    try:
        n = int(val)
        return list(range(1, n + 1))
    except ValueError:
        return list(range(1, default_count + 1))


def populate_order_csv():
    """Generate `order_data.csv` with columns: order_id, receipt_id, item_id.

    Behavior:
    - Generates receipts with IDs 1..NUM_RECEIPTS (config via env var `ORDER_NUM_RECEIPTS`).
    - Each receipt gets a random number of items drawn from a skewed distribution so most receipts have 1 item and some have more.
    - Item IDs are chosen from a menu (default 1..50) or from the env var `ORDER_MENU_ITEMS` (comma-separated or single integer meaning 1..N).
    - Writes rows streaming to avoid large memory usage.
    """
    # Configurable via environment variables
    NUM_RECEIPTS = parse_int('ORDER_NUM_RECEIPTS', 1000000)
    OUTPUT_FILENAME = os.environ.get('ORDER_OUTPUT', 'csv_data/order_data.csv')
    # Default menu size
    menu_items = parse_menu_items('ORDER_MENU_ITEMS', 20)

    # Distribution of items-per-receipt: probabilities for 1..5 items
    # Majority single-item receipts, some with multiple items
    items_options = [1, 2, 3, 4, 5]
    items_probs = [0.70, 0.20, 0.07, 0.02, 0.01]

    # If user provided ORDER_MAX_ITEMS, trim the distribution
    max_items = parse_int('ORDER_MAX_ITEMS', 5)
    if max_items < 5:
        items_options = [i for i in items_options if i <= max_items]
        items_probs = items_probs[: len(items_options)]
        # normalize
        s = sum(items_probs)
        items_probs = [p / s for p in items_probs]

    print(f"Generating {NUM_RECEIPTS} receipts -> writing {OUTPUT_FILENAME}")
    print(f"Menu items: {len(menu_items)} (sample: {menu_items[:5]})")

    order_id = 0
    total_rows = 0

    with open(OUTPUT_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ORDER_ID', 'RECEIPT_ID', 'ITEM_ID'])

        for receipt_id in range(1, NUM_RECEIPTS + 1):
            # choose how many items this receipt has
            num_items = random.choices(items_options, weights=items_probs, k=1)[0]
            for _ in range(num_items):
                order_id += 1
                item_id = random.choice(menu_items)
                writer.writerow([order_id, receipt_id, item_id])
            total_rows += num_items

    print(f"Wrote {order_id} order rows for {NUM_RECEIPTS} receipts (total items: {total_rows})")
    print(f"Saved to: {os.path.abspath(OUTPUT_FILENAME)}")

def populate_receipt_csv():
    """
    Script to populate a CSV file with 1000 entries of generated data.
    """
    
    # =================================
    # COLUMN HEADINGS CONFIGURATION
    # =================================
    # Define your column headers here
    column_headers = [
        "RECEIPT_ID",
        "EMPLOYEE_ID",
        # "e_first_name",
        # "e_last_name",
        # "e_password",
        "CUSTOMER_ID",
        # "c_first_name",
        # "c_last_name",
        # "c_phone",
        # "c_points",
       
        # "cost",
        "TIP",
        "ORDER_TIME",
        "ORDER_DATE",
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
    
    # Customer data (weighted random - some customers visit much more frequently)
    c_ids = []
    c_first_name_list = []
    c_last_name_list = []
    c_phone_list = []
    
    # Create weighted distribution: some customers are frequent, others rare
    # Use exponential decay to create realistic customer frequency distribution
    weights = []
    for i in range(len(customer_records)):
        # Higher weight for earlier customers, exponential decay for later ones
        weight = (len(customer_records) - i) ** 1.5  # Power > 1 creates more skew
        weights.append(weight)
    
    for i in range(NUM_ENTRIES):
        cust_record = random.choices(customer_records, weights=weights, k=1)[0]
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
    csv_filename = "csv_data/receipt_data.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
    
    # Combine all lists into rows
    data_rows = []
    for i in range(NUM_ENTRIES):
        row = [
            receipt_ids[i],
            e_ids[i],
            # e_first_name_list[i],
            # e_last_name_list[i],
            # e_password_list[i],
            c_ids[i],
            # c_first_name_list[i],
            # c_last_name_list[i],
            # c_phone_list[i],
            # c_points_list[i],
           
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

def populate_recipe_csv(output_filename: str = "csv_data/recipes.csv"):
    """Create a CSV file containing the recipe mappings.

    Columns: RecipeID, ItemID, IngredientID
    """

    headers = ["ITEM_ID", "INGREDIENT_ID"]

    recipes = [
        (9, 2),
        (10, 3),
        (11, 4),
        (12, 5),
        (13, 6),
        (0, 0),
        (0, 1),
        (0, 11),
        (0, 12),
        (0, 13),
        (0, 14),
        (0, 15),
        (0, 16),
        (1, 0),
        (1, 1),
        (1, 15),
        (1, 16),
        (1, 17),
        (1, 18),
        (2, 0),
        (2, 1),
        (2, 11),
        (2, 15),
        (2, 16),
        (3, 0),
        (3, 1),
        (3, 15),
        (3, 16),
        (3, 19),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 11),
        (4, 12),
        (4, 15),
        (4, 16),
        (4, 20),
        (5, 0),
        (5, 1),
        (5, 11),
        (5, 15),
        (5, 16),
        (5, 21),
        (6, 0),
        (6, 1),
        (6, 15),
        (6, 16),
        (6, 22),
        (7, 0),
        (7, 1),
        (7, 15),
        (7, 16),
        (7, 22),
        (7, 23),
        (8, 0),
        (8, 1),
        (8, 15),
        (8, 16),
        (8, 22),
        ( 8, 23),
        ( 8, 24),
        ( 8, 25),
        ( 8, 26),
        (8, 27),
        (14, 0),
        (14, 1),
        (14, 16),
        (14, 24),
        (14, 26),
        (15, 0),
        (15, 1),
        (15, 18),
        (15, 24),
        (15, 26),
        (16, 0),
        (16, 1),
        (16, 11),
        (16, 16),
        (16, 24),
        (16, 28),
        (17, 0),
        (17, 1),
        (17, 8),
        (17, 12),
        (17, 16),
        (18, 0),
        (18, 1),
        (18, 16),
        (18, 12),
        (18, 24),
        (18, 29),
        (19, 0),
        (19, 1),
        (19, 12),
        (19, 16),
        (19, 24),
        (19, 7),
        (20, 0),
        (20, 1),
        (20, 11),
        (20, 16),
        (20, 18),
        (20, 24),
    ]

    csv_filepath = os.path.join(os.getcwd(), output_filename)

    try:
        with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(recipes)

    except Exception as e:
        print(f"Error writing recipe CSV: {e}")
    else:
        print(f"Wrote {len(recipes)} recipe mappings to: {csv_filepath}")

if __name__ == "__main__":
    populate_employee_records()
    populate_customer_csv()
    populate_ingredients_csv()
    populate_sharetea_menu()
    populate_order_csv()
    populate_receipt_csv()
    populate_recipe_csv()

