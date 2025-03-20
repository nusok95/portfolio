from datetime import datetime, timedelta
import random


def generate_stock_prices(start_date, end_date, initial_price):
    prices = {}
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    current_price = initial_price

    while current_date <= end_date:
        prices[current_date.strftime("%Y-%m-%d")] = round(current_price, 2)
        
        fluctuation = random.uniform(-0.10, 0.10)
        current_price *= (1 + fluctuation)
        
        current_date += timedelta(days=1)

    return prices
