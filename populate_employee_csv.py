import csv
import os


def populate_sharetea_menu(output_filename: str = "csv_data\employee_records.csv"):
    """Create a CSV file containing the Gong Cha Employees.

    Columns: Employee ID, First Name, Last Name, Password
    """

    headers = ["Employee_ID", "First_Name", "Last_Name", "Password"]

    # ItemCost stored as integer cents (e.g. $5.65 => 565). Empty/unknown costs => 0
    menu_records = [
        (0, "Allen", "Basil", "Basil"),
        (1, "Gauri", "Agrawal", "Agrawal"),
        (2, "Hiya", "Sharma", "Sharma"),
        (3, "David", "Hunt", "Hunt"),
        (4, "Orlando", "Haye", "Haye"),
        (5, "Jayden", "Cox", "Cox"),
        (6, "Paul", "Taele", "Taele"),
        
    ]

    csv_filepath = os.path.join(os.getcwd(), output_filename)

    try:
        with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(menu_records)

    except Exception as e:
        print(f"Error writing menu CSV: {e}")
    else:
        print(f"Wrote {len(menu_records)} menu items to: {csv_filepath}")


if __name__ == "__main__":
    populate_sharetea_menu()

