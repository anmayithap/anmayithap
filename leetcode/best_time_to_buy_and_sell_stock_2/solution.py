def max_profit(prices: list[int]) -> int:
    prices[:] = [
        prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] - prices[i - 1] > 0
    ]
    return sum(prices)
