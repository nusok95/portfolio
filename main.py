from stock_generator import generate_stock_prices
from portfolio import Portfolio
from stock import Stock

AVAILABLE_STOCKS = {
    1: {"symbol": "MSFT", "initial_price": 300.0},
    2: {"symbol": "AAPL", "initial_price": 150.0},
    3: {"symbol": "TSLA", "initial_price": 700.0},
    4: {"symbol": "GOOGL", "initial_price": 2800.0},
    5: {"symbol": "AMZN", "initial_price": 3400.0},
}

def display_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Ver composición del portafolio")
    print("2. Agregar stock al portafolio")
    print("3. Mostrar profit del portafolio entre dos fechas")
    print("4. Mostrar rendimiento anualizado entre dos fechas")
    print("5. Salir")
    return input("Selecciona una opción (1-5): ")

def list_available_stocks():
    print("Stocks disponibles:")
    for number, stock in AVAILABLE_STOCKS.items():
        print(f"{number}. {stock['symbol']}")

def add_stock_to_portfolio(portfolio):
    list_available_stocks()
    try:
        choice = int(input("Selecciona el número del stock que deseas agregar: "))
        if choice in AVAILABLE_STOCKS:
            stock_data = AVAILABLE_STOCKS[choice]
            symbol = stock_data["symbol"]
            initial_price = stock_data["initial_price"]

            prices = generate_stock_prices("2025-02-01", "2025-03-19", initial_price)
            
            stock = Stock(symbol, prices)
            portfolio.add_stock(stock)
            print(f"\nStock {symbol} agregado al portafolio.")
        else:
            print("\nOpción no válida. Intenta de nuevo.")
    except ValueError:
        print("\nEntrada no válida. Debes ingresar un número.")

def show_portfolio_composition(portfolio):
    if not portfolio.stocks:
        print("\nTu portafolio está vacío.")
    else:
        print("\nComposición del portafolio:")
        for stock in portfolio.stocks:
            print(f"- {stock.symbol}")

def calculate_profit(portfolio):
    start_date = input("Ingresa la fecha inicial (YYYY-MM-DD): ")
    end_date = input("Ingresa la fecha final (YYYY-MM-DD): ")
    try:
        profit = portfolio.profit(start_date, end_date)
        print(f"\nProfit entre {start_date} y {end_date}: ${profit:.2f}")
    except Exception as e:
        print(f"\nError: {e}")

def calculate_annualized_return(portfolio):
    start_date = input("Ingresa la fecha inicial (YYYY-MM-DD): ")
    end_date = input("Ingresa la fecha final (YYYY-MM-DD): ")
    try:
        annualized_return = portfolio.AnnualizedReturn(start_date, end_date)
        print(f"\nRendimiento anualizado entre {start_date} y {end_date}: {annualized_return:.2%}")
    except Exception as e:
        print(f"\nError: {e}")

def main():
    portfolio = Portfolio()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            show_portfolio_composition(portfolio)
        elif choice == "2":
            add_stock_to_portfolio(portfolio)
        elif choice == "3":
            calculate_profit(portfolio)
        elif choice == "4":
            calculate_annualized_return(portfolio)
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
