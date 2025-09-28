import csv
import os


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


if __name__ == "__main__":
    populate_ingredients_csv()

