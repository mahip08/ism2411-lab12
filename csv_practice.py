
# Reflection

# 1. Python makes it easier to automate repetitive tasks, process large amounts of data, and make reports without doing everything
# manually. Excel is useful when organizing data, making charts, and quickly viewing information in spreadsheets.

# 2. A business could use an append-mode log to track daily sales transactions. Append mode is useful because it saves each new
# entry without deleting past records, helping the business keep a history of its sales.

import csv
from datetime import datetime


# EXERCISE 1
with open("data/sales.csv", "r") as file:
    print("Sales file opened successfully!")


# EXERCISE 2
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4
total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")


# EXERCISE 5
original_count = 0
written_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")


# EXERCISE 6
dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nDictReader total revenue: ${dict_total_revenue:.2f}")

# csv.reader accesses columns using numerical indexes.
# csv.DictReader accesses columns by name, making it easier to understand labeled data.


# EXERCISE 7
sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8
with open("data/run_log.txt", "a") as log_file:
    timestamp = datetime.now()
    log_file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print("Run log updated!")
