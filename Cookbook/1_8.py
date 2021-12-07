# opearation in dict
# zip

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

prices_sorted = sorted(zip(prices.values(),prices.keys()), reverse=True)
print(prices_sorted)