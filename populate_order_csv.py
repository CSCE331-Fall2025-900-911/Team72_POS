import csv
import os
import random
from typing import List


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
    OUTPUT_FILENAME = os.environ.get('ORDER_OUTPUT', 'order_data.csv')
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
        writer.writerow(['order_id', 'receipt_id', 'item_id'])

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


if __name__ == '__main__':
    populate_order_csv()
