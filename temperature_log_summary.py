records = [('Mon', 125), ('Tue', 230), ('Wed', 90)]
total = sum(amount for _, amount in records)
for name, amount in records:
    print(f"{name}: {amount}")
print("Total:", total)
print("Average:", round(total / len(records), 2))

