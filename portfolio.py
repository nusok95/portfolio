from datetime import datetime

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def profit(self, start_date, end_date):
        total_profit = 0.0
        for stock in self.stocks:
            start_price = stock.price(start_date)
            end_price = stock.price(end_date)
            total_profit += (end_price - start_price)
        return total_profit

    def annualized_return(self, start_date, end_date):
        total_profit = self.profit(start_date, end_date)
        initial_investment = self._get_initial_investment(start_date)
        
        if initial_investment == 0:
            return 0.0

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        years = (end_date - start_date).days / 365.25
        
        if years == 0:
            return 0.0
        
        annualized_return = ((1 + (total_profit / initial_investment)) ** (1 / years)) - 1
        return annualized_return
    
    def _get_initial_investment(self, start_date):
        return sum(stock.price(start_date) for stock in self.stocks)
