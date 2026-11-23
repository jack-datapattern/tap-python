import csv
def read(file):
    with open(file,"r") as f:
        r=csv.DictReader(f)
        rows=[]
        for i, row in enumerate(r):
            if i == 5:
                break
            rows.append(row)
    return rows



import csv
def read_csv(path):
    with open(path, "r") as file:
        return list(csv.DictReader(file))

    