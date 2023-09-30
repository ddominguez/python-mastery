import csv


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            records.append((route, date, daytype, rides))
    return records


def read_rides_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            records.append(
                {"route": route, "date": date, "daytype": daytype, "rides": rides}
            )
    return records


# class Row:
#     __slots__ = ["route", "date", "daytype", "rides"]
#
#     def __init__(self, route, date, daytype, rides):
#         self.route = route
#         self.date = date
#         self.daytype = daytype
#         self.rides = rides


# Uncomment to use a namedtuple instead
from collections import namedtuple

Row = namedtuple("Row", ("route", "date", "daytype", "rides"))


def read_rides_as_class_objects(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            records.append(Row(route, date, daytype, rides))
    return records


# as tuples:
# Memory Use: Current 123687918, Peak 123718416

# as dicts:
# Memory Use: Current 188372982, Peak 188403480

# as class objects:
# Memory Use: Current 142173182, Peak 142203680

# as class objects with slots:
# Memory Use: Current 119067902, Peak 119098400

# as namedtuples:
# Memory Use: Current 128308806, Peak 128339304

if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    # rows = read_rides_as_tuples("../Data/ctabus.csv")
    # rows = read_rides_as_dicts("../Data/ctabus.csv")
    rows = read_rides_as_class_objects("../Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
