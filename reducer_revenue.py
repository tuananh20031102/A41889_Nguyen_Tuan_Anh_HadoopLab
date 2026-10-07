import sys

current_category = None
total = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    category, amount = line.split("\t")
    amount = int(amount)

    if current_category == category:
        total += amount
    else:
        if current_category is not None:
            print(f"{current_category}\t{total}")

        current_category = category
        total = amount

if current_category is not None:
    print(f"{current_category}\t{total}")
