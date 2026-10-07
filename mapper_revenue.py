import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    if row["status"] == "SUCCESS":
        category = row["category"]
        amount = int(row["amount"])
        print(f"{category}\t{amount}")
