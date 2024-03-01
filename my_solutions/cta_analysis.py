import readrides
from collections import Counter, defaultdict

rows = readrides.read_rides_as_dicts("../Data/ctabus.csv")
# {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}


# -------------------------------------
# How many bus routes exist in Chicago?
unique_bus_routes = {row["route"] for row in rows}
print("How many bus routes exist in Chicago?")
print(f"- {len(unique_bus_routes)}\n")


# -------------------------------------
# How many people rode the number 22 bus on February 2, 2011?
# What about any route on any date of your choosing?
rides_by_route_date = {}
for row in rows:
    rides_by_route_date[row["route"], row["date"]] = row["rides"]

print("How many people rode the number 22 bus on February 2, 2011?")
print(f'- {rides_by_route_date["22", "02/02/2011"]}\n')


# -------------------------------------
# What is the total number of rides taken on each bus route?
# total_rides_per_bus_route = Counter()
# for row in rows:
#     total_rides_per_bus_route[row["route"]] += row["rides"]

# for k, v in total_rides_per_bus_route.items():
#     print(f"Bus route: {k}, Total rides: {v}")


# -------------------------------------
# What five bus routes had the greatest ten-year increase in ridership from
# 2001 to 2011?
# create mapping :
# {'ROUTE, 2001': RIDES_COUNT}
# {'ROUTE, 2011': RIDES_COUNT}
bus_route_rides_in_2001 = Counter()
bus_route_rides_in_2011 = Counter()

for row in rows:
    y = row["date"].split("/")[2]
    if y == "2001":
        bus_route_rides_in_2001[row["route"]] += row["rides"]
    elif y == "2011":
        bus_route_rides_in_2011[row["route"]] += row["rides"]

bus_route_diffs = Counter()
for route, rides in bus_route_rides_in_2011.items():
    bus_route_diffs[route] = rides - bus_route_rides_in_2001.get(route, 0)

print(bus_route_diffs.most_common(5))
