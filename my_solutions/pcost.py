def portfolio_cost(filename: str) -> float:
    total_cost = 0.0
    with open(filename, "r") as f:
        for line in f:
            split = line.strip().split(" ")
            name = split[0]
            try:
                shares = int(split[1])
                price = float(split[2])
            except ValueError as e:
                print(f"Couldn't parse: '{line.strip()}'")
                print(f"Reason: {e}")
                continue

            total_cost += shares * price
    return total_cost


if __name__ == "__main__":
    print(portfolio_cost("../Data/portfolio.dat"))
