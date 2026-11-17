stock = {'Pens': 12, 'Paper': 3, 'Ink': 1}
low = [name for name, qty in stock.items() if qty < 5]
print('Reorder:', ', '.join(low))

