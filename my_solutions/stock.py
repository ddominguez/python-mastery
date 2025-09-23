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

Exercise 6.1
- redefined Stock class using Structure class
"""

from structure import Structure


class Stock(Structure):
    _fields = ("name", "shares", "price")

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
