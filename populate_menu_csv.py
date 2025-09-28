import csv
import os


def populate_sharetea_menu(output_filename: str = "sharetea_menu.csv"):
    """Create a CSV file containing the Sharetea menu items.

    Columns: Item ID, Item Name, Item Category, Item Cost, Ingredients
    """

    # Use the exact menu requested; ItemCost stored as integer cents (e.g. $5.75 -> 575)
    headers = ["ItemID", "ItemName", "ItemCategory", "ItemCost"]
    
    menu_records = [
        (0, "Wintermelon Milk Tea", "Milk Tea", 575),
        (1, "Strawbery Milk Tea", "Milk Tea", 575),
        (2, "Milk Black Tea", "Milk Tea", 575),
        (3, "Oolong Tea", "Milk Tea", 575),
        (4, "Pearl Milk Tea", "Milk Tea", 575),
        (5, "Caramel Milk Tea", "Milk Tea", 550),
        (6, "Milk Coffee", "Coffee", 550),
        (7, "Coffee Milk Tea", "Coffee", 550),
        (8, "Milk Foam Black Coffee", "Coffee", 600),
        (9, "Pearl", "Toppings", 75),
        (10, "Coconut Jelly", "Toppings", 75),
        (11, "Herbal Jelly", "Toppings", 75),
        (12, "Ai-Yu Jelly", "Toppings", 75),
        (13, "White Pearl", "Toppings", 100),
        (14, "Matcha Tea Latte", "Tea Latte", 575),
        (15, "Strawberry Matcha Latte", "Tea Latte", 650),
        (16, "Thai Tea Latte", "Tea Latte", 625),
        (17, "Lychee", "Slush Series", 675),
        (18, "Taro Milk", "Slush", 675),
        (19, "Mango Milk", "Slush Series", 675),
        (20, "Strawberry Mik", "Slush Series", 675),
    ]

    csv_filepath = os.path.join(os.getcwd(), output_filename)

    try:
        with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            # write rows ensuring cost is integer
            for item in menu_records:
                item_id, name, category, cost = item
                writer.writerow([item_id, name, category, int(cost)])

    except Exception as e:
        print(f"Error writing menu CSV: {e}")
    else:
        print(f"Wrote {len(menu_records)} menu items to: {csv_filepath}")


if __name__ == "__main__":
    populate_sharetea_menu()