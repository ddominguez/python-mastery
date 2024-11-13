"""
Python Mastery

Exercise 3.3
- added read_csv_as_instances()

Exercise 3.7
- added csv parser abstract class
- added csv parsers that parses into dicts and instances

Exercise 5.1
- revert to simple functions
- added type hints

Exercise 5.3
- added convert_csv
- updated csv_as_ funcs to use convert_csv func
"""

import csv
from collections.abc import Callable
from typing import TextIO


def csv_as_dicts(
    file: TextIO,
    types: list[Callable],
    headers: list[str] | None = None,
):
    """
    Convert CSV file data into a list of dictionaries with optional type conversion.
    """

    def convert_func(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(file, convert_func, headers)


def csv_as_instances(file: TextIO, cls, headers=None):
    """
    Convert CSV file data into a list of instances.
    """

    def convert_func(headers, row):
        return cls.from_row(row)

    return convert_csv(file, convert_func, headers)


def convert_csv(lines, convert_func, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return [convert_func(headers, row) for row in rows]


def read_csv_as_dicts(
    filename: str,
    types: list[Callable],
    headers: list[str] | None = None,
):
    """
    Read CSV data into a list of dictionaries with optional type conversion.
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)


def read_csv_as_instances(filename: str, cls, headers=None):
    """
    Read CSV data into a list of instances.
    """
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
