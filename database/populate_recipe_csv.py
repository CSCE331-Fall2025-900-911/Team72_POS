import csv
import os


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
    populate_recipe_csv()
