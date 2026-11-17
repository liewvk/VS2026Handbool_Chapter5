orders = [('Books', 35), ('Food', 20), ('Books', 25)]
totals = {}
for category, amount in orders:
    totals[category] = totals.get(category, 0) + amount
print(totals)

