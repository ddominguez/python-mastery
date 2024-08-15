"""
Python Mastery

Exercise 3.3
- added from_row class method
- removed read_portfolio()

Exercise 3.4
- convert types to private attr _types
- update cost() to property
- enforce validation for shares and price
- restrictes attr names using slots
- update property definition to use _types

Exercise 3.6
- added __repr__() and __eq__()
"""


class Stock:
    __slots__ = ("name", "_shares", "_price")
    _types = (str, int, float)

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return (
            f"{type(self).__name__}('{self.name!r}', {self.shares!r}, {self.price!r})"
        )

    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price)
            == (other.name, other.shares, other.price)
        )

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        attr_type = self._types[1]
        if not isinstance(value, attr_type):
            raise TypeError(f"expected {attr_type.__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        attr_type = self._types[2]
        if not isinstance(value, attr_type):
            raise TypeError(f"expected {attr_type.__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    @property
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
