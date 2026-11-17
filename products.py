products = {"P001": 12.50, "P002": 8.00}
for code, price in products.items():
 print(f"{code}: RM{price:.2f}")
print("P001 exists:", "P001" in products)

