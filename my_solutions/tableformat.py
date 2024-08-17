"""
Python Mastery

Exercise 3.2
- added print_table()


Exercise 3.5
- added TableFormatter classes

Exercise 3.7
- convert TableFormatter to abstract base class

Exercise 3.8
- added format mixins
"""

from abc import ABC, abstractmethod


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


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


def create_formatter(name, column_formats=None, upper_headers=False):
    """Returns a table formatter."""
    if name == "text":
        formatter_cls = TextTableFormatter
    elif name == "csv":
        formatter_cls = CSVTableFormatter
    elif name == "html":
        formatter_cls = HTMLTableFormatter
    else:
        raise ValueError("expected text, csv, or html")

    if column_formats:

        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:

        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()


def print_table(records, fields, formatter):
    """Prints a nicely formatted table."""
    if not isinstance(formatter, TableFormatter):
        raise TypeError("expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
