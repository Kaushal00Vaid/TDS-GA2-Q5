import json

with open("products.json") as f:
    data = json.load(f)

sports_products = [p for p in data["products"] if p["category"] == "sports"]

count = len(sports_products)
inventory_value = sum(p["price"] * p["stock"] for p in sports_products)

print(f"Sports count: {count}")
print(f"Sports inventoryValue: {inventory_value:.2f}")