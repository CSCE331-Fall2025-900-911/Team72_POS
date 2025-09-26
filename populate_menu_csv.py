import csv
import os


def populate_sharetea_menu(output_filename: str = "sharetea_menu.csv"):
    """Create a CSV file containing the Sharetea menu items.

    Columns: Item ID, Item Name, Item Category, Item Cost, Ingredients
    """

    headers = ["ItemID", "ItemName", "ItemCategory", "ItemCost", "Ingredients"]

    # ItemCost stored as integer cents (e.g. $5.65 => 565). Empty/unknown costs => 0
    menu_records = [
        (0, "Wintermelon", "Milk Foam", 565, ""),
        (1, "Green Tea", "Milk Foam", 0, ""),
        (2, "Black Tea", "Milk Foam", 0, ""),
        (3, "Oolong Tea", "Milk Foam", 0, ""),
        (4, "Pearl Milk Tea", "Milk Tea", 580, ""),
        (5, "Caramel Milk Tea", "Milk Tea", 0, ""),
        (6, "Milk Coffee", "Milk Tea", 0, ""),
        (7, "Coffee Milk Tea", "Milk Tea", 625, ""),
        (8, "Milk Foam Black Coffee", "Coffee", 0, ""),
        (9, "Stuff", "Coffee", 0, ""),
        (10, "Stuff23", "Coffee", 0, ""),
        (11, "Match Pearl Milk Tea", "Matcha", 650, ""),
        (12, "Mango Match Fresh Milk", "Matcha", 650, ""),
        (13, "Strawberry Matcha Fresh Milk", "Matcha", 650, ""),
        (14, "Match Fresh Milk", "Matcha", 625, ""),
        (15, "Match Ice Blended", "Matcha", 650, ""),
        (16, "Peach Tea w/ Honey Jelly (Black/Green/Oolong Tea)", "Fruity Beverage", 625, ""),
        (17, "Honey Lemonade", "Fruity Beverage", 520, ""),
        (18, "Mango Green Tea", "Fruity Beverage", 580, ""),
        (19, "Mango & Passion Fruit Tea", "Fruity Beverage", 625, ""),
        (20, "Berry Lychee Burst", "Fruity Beverage", 625, ""),
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

