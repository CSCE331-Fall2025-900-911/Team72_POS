import csv
import os


def populate_sharetea_menu(output_filename: str = "csv_data/employee_records.csv"):
    """Create a CSV file containing the Gong Cha Employees.

    Columns: Employee ID, First Name, Last Name, Password
    """

    headers = ["Employee_ID", "First_Name", "Last_Name", "Password"]

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


if __name__ == "__main__":
    populate_sharetea_menu()

