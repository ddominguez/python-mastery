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

Exercise 5.5
- added error handling to convert csv
"""

import csv
import logging
from collections.abc import Callable
from typing import TextIO

log = logging.getLogger(__name__)


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
    result = []
    for row_num, row in enumerate(rows, start=1):
        try:
            result.append(convert_func(headers, row))
        except ValueError as e:
            log.warning(f"Row {row_num}: Bad row: {row}")
            log.debug(f"Row {row_num}: Reason: {e}")
    return result


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
