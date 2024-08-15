"""
Python Mastery

Exercise 3.2
- added print_table()


Exercise 3.5
- added TableFormatter classes

Exercise 3.7
- convert TableFormatter to abstract base class
"""

from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join(f"{h:>10}" for h in headers))
        print(" ".join("-" * 10 for _ in range(len(headers))))

    def row(self, rowdata):
        print(" ".join(f"{d:>10}" for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(h for h in headers))

    def row(self, rowdata):
        print(",".join(f"{d}" for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", " ".join(f"<th>{h}</th>" for h in headers), "</tr>")

    def row(self, rowdata):
        print("<tr>", " ".join(f"<td>{d}</td>" for d in rowdata), "</tr>")


def create_formatter(name: str):
    """Returns a table formatter."""
    if name == "text":
        formatter_cls = TextTableFormatter
    elif name == "csv":
        formatter_cls = CSVTableFormatter
    elif name == "html":
        formatter_cls = HTMLTableFormatter
    else:
        raise ValueError("expected text, csv, or html")
    return formatter_cls()


def print_table(records, fields, formatter):
    """Prints a nicely formatted table."""
    if not isinstance(formatter, TableFormatter):
        raise TypeError("expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
