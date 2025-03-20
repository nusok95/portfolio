class Stock:
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.prices = prices

    def price(self, date):
        return self.prices.get(date, 0.0)
