orders = [75, 140, 290, 510]
for amount in orders:
    rate = 0.15 if amount >= 300 else 0.05 if amount >= 100 else 0.0
    payable = amount * (1 - rate)
    print(f'Order RM{amount:.2f} -> RM{payable:.2f}')
