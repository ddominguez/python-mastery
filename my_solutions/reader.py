import csv


def read_csv_as_dicts(filename: str, coltypes: list):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(
                {name: func(val) for name, func, val in zip(headers, coltypes, row)}
            )

    return records
