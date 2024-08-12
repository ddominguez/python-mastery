"""
Python Mastery

Exercise 3.2
"""

COLUMN_WIDTH = 10


def print_table(objects: list[object], attributes: list[str]):
    """
    Takes a sequence (list) of objects, a list of attribute names,
     and prints a nicely formatted table.
    """
    print(" ".join(f"{attr:>{COLUMN_WIDTH}}" for attr in attributes))
    print(" ".join("-" * COLUMN_WIDTH for _ in range(len(attributes))))
    for obj in objects:
        print(" ".join(f"{getattr(obj, attr):>{COLUMN_WIDTH}}" for attr in attributes))
