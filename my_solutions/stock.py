"""
Python Mastery

Exercise 3.3
- added from_row class method
- removed read_portfolio()
"""


class Stock:
    types = (str, int, float)

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares


def print_portfolio(stocks):
    """Print portfolio in a formatted table."""

    print("%10s %10s %10s" % ("name", "shares", "price"))
    print((("-" * 10) + " ") * 3)
    for s in stocks:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
