stock = {'Keyboard': 12, 'Mouse': 4, 'Monitor': 2, 'USB hub': 7}
threshold = 5
for product, quantity in stock.items():
    if quantity < threshold:
        print(f'Reorder {product}: only {quantity} left')

