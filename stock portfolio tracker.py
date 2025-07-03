# stock_tracker.py

# Step 1: Define stock prices (dictionary)
stock_prices = {
    'AAPL': 195.20,
    'GOOGL': 2815.67,
    'TSLA': 695.30,
    'AMZN': 3301.12,
    'INFY': 1502.45
}

# Step 2: Initialize investment dictionary
portfolio = {}
total_investment = 0

print("Welcome to the Stock Tracker!")
print("Available stocks:", ', '.join(stock_prices.keys()))

# Step 3: Input number of shares owned
for stock, price in stock_prices.items():
    try:
        quantity = int(input(f"How many shares of {stock} do you own? "))
    except ValueError:
        print("Invalid input. Defaulting to 0.")
        quantity = 0

    investment = quantity * price
    portfolio[stock] = (quantity, investment)
    total_investment += investment

# Step 4: Output results to terminal
print("\n--- Your Portfolio Summary ---")
for stock, (qty, invest) in portfolio.items():
    print(f"{stock}: {qty} shares -> ₹{invest:.2f}")
print(f"\nTotal Investment: ₹{total_investment:.2f}")

# Step 5: Save results to file
with open("portfolio_summary.txt", "w") as file:
    file.write("--- Your Portfolio Summary ---\n")
    for stock, (qty, invest) in portfolio.items():
        file.write(f"{stock}: {qty} shares -> ₹{invest:.2f}\n")
    file.write(f"\nTotal Investment: ₹{total_investment:.2f}\n")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")
