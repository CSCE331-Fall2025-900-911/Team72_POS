import csv
import os


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


if __name__ == "__main__":
    populate_sharetea_menu()