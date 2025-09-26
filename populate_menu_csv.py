import csv
import os
import random
import csv
import os


def populate_sharetea_menu(output_filename: str = "sharetea_menu.csv"):
    """Create a CSV file containing the Sharetea menu items.

    Columns: Item ID, Item Name, Item Category, Item Cost, Ingredients
    """

    headers = ["Item ID", "Item Name", "Item Category", "Item Cost", "Ingredients"]

    menu_records = [
        (0, "Wintermelon", "Milk Foam", "5.65", ""),
        (1, "Green Tea", "Milk Foam", "", ""),
        (2, "Black Tea", "Milk Foam", "", ""),
        (3, "Oolong Tea", "Milk Foam", "", ""),
        (4, "Pearl Milk Tea", "Milk Tea", "5.80", ""),
        (5, "Caramel Milk Tea", "Milk Tea", "", ""),
        (6, "Milk Coffee", "Milk Tea", "", ""),
        (7, "Coffee Milk Tea", "Milk Tea", "6.25", ""),
        (8, "Milk Foam Black Coffee", "Coffee", "", ""),
        (9, "", "Coffee", "", ""),
        (10, "", "Coffee", "", ""),
        (11, "Match Pearl Milk Tea", "Matcha", "6.50", ""),
        (12, "Mango Match Fresh Milk", "Matcha", "6.50", ""),
        (13, "Strawberry Matcha Fresh Milk", "Matcha", "6.50", ""),
        (14, "Match Fresh Milk", "Matcha", "6.25", ""),
        (15, "Match Ice Blended", "Matcha", "6.50", ""),
        (16, "Peach Tea w/ Honey Jelly (Black/Green/Oolong Tea)", "Fruity Beverage", "6.25", ""),
        (17, "Honey Lemonade", "Fruity Beverage", "5.20", ""),
        (18, "Mango Green Tea", "Fruity Beverage", "5.80", ""),
        (19, "Mango & Passion Fruit Tea", "Fruity Beverage", "6.25", ""),
        (20, "Berry Lychee Burst", "Fruity Beverage", "6.25", ""),
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

