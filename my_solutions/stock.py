import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares


def read_portfolio(portfolio_file):
    """Reads a file of portfolio data into a list of Stock objects."""

    stocks = []
    with open(portfolio_file) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for name, shares, price in rows:
            stocks.append(Stock(name, int(shares), float(price)))
    return stocks


def print_portfolio(stocks):
    """Print portfolio in a formatted table."""

    print("%10s %10s %10s" % ("name", "shares", "price"))
    print((("-" * 10) + " ") * 3)
    for s in stocks:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
