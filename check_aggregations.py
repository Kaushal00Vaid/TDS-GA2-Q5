import json
from collections import defaultdict

with open("products.json") as f:
    data = json.load(f)

# group stats per category
stats = defaultdict(lambda: {"count": 0, "inventoryValue": 0.0})

for p in data["products"]:
    cat = p["category"]
    stats[cat]["count"] += 1
    stats[cat]["inventoryValue"] += p["price"] * p["stock"]

# pretty print results
for category, info in stats.items():
    print(f"Category: {category}")
    print(f"  count: {info['count']}")
    print(f"  inventoryValue: {info['inventoryValue']:.2f}")
    print()