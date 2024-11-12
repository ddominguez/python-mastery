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
    records = []
    rows = csv.reader(file)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(file: TextIO, cls, headers=None):
    """
    Convert CSV file data into a list of instances.
    """
    records = []
    rows = csv.reader(file)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


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
