"""
Python Mastery

Exercise 3.3
- added read_csv_as_instances()
"""

import csv


def read_csv_as_dicts(filename: str, coltypes: list):
    """Read a CSV file into a list of dicts."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(
                {name: func(val) for name, func, val in zip(headers, coltypes, row)}
            )

    return records


def read_csv_as_instances(filename, cls):
    """Read a CSV file into a list of instances."""

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
