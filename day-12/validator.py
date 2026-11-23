import csv
def valid(file):
    with open(file,"r") as f:
        r=csv.DictReader(f)
        order_ids = [row["order_id"] for row in r]

    return len(order_ids) == len(set(order_ids))
