def max_profit(prices: list[int]) -> int:
    min_price, max_profit = float('inf'), float('-inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, (price - min_price))

    return int(max_profit)
