"""
Python Mastery

Exercise 5.6
- added teststock.py
"""

import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_kwargs(self):
        s = stock.Stock(price=490.1, name="GOOG", shares=100)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        shares = 100
        price = 490.1
        s = stock.Stock("GOOG", shares, price)
        self.assertEqual(s.cost, shares * price)

    def test_sell(self):
        shares = 100
        price = 490.1
        s = stock.Stock("GOOG", shares, price)
        self.assertEqual(s.shares, shares)
        shares_sold = 10
        s.sell(shares_sold)
        self.assertEqual(s.shares, shares - shares_sold)

    def test_from_row(self):
        row = ["GOOG", 10, 490.1]
        s = stock.Stock.from_row(row)
        self.assertEqual(s.name, row[0])
        self.assertEqual(s.shares, row[1])
        self.assertEqual(s.price, row[2])

    def test_repr(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        s1 = stock.Stock("GOOG", 100, 490.1)
        s2 = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s1, s2)

    def test_shares_type_error(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = "50"

    def test_shares_value_error(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -100

    def test_price_type_error(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = "50"

    def test_price_value_error(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -490.1

    def test_non_existent_attribute(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 40


if __name__ == "__main__":
    unittest.main()
