class StockAnalyzer:
    def __init__(self, prices):
        self.prices = prices

    def calculate_max_profit(self):
        min_price = self.prices[0]
        max_profit = 0

        for price in self.prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

    def calculate_volatility_index(self):
        total_difference = 0
        for i in range(len(self.prices) - 1):
            total_difference += abs(self.prices[i + 1] - self.prices[i])

        return round(total_difference / (len(self.prices) - 1), 2)

try:
    print("=" * 40)
    print("Enter stock prices separated by space:")
    print("=" * 40)
    prices = list(map(int, input().split()))

    if len(prices) < 2:
        print("Max Profit: 0")
        print("Volatility Index: 0.00")
    else:
        analyzer = StockAnalyzer(prices)

        max_profit = analyzer.calculate_max_profit()
        volatility = analyzer.calculate_volatility_index()

        print("Max Profit:", max_profit)
        print("Volatility Index:", format(volatility, ".2f"))

except Exception as e:
    print("Invalid input. Please enter valid stock prices.")