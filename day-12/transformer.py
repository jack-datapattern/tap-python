import csv

def convert_prices(file):
    with open(file, "r") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        row["price"] = float(row["price"])
        row["freight_value"] = float(row["freight_value"])

    return rows
