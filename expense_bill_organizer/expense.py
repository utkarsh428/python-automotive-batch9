import csv
import os
from datetime import date

file = "expenses.csv"

# create csv file 
if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount"])

while True:
    print("\nExpense Bill Organizer")
    print("1. Save bill")
    print("2. Category wise total")
    print("3. Monthly report")
    print("4. Exit")

    choice = input("Enter choice: ")

    # 1. Save bill
    if choice == "1":
        d = input("Enter date (YYYY-MM-DD) or Enter for today: ")
        if d == "":
            d = str(date.today())

        cat = input("Enter category: ")
        amt = float(input("Enter amount: "))

        with open(file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([d, cat, amt])

        print("Bill saved")

    # 2. total (category-wise)
    elif choice == "2":
        totals = {}

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                category = row["category"]
                amount = float(row["amount"])

                if category in totals:
                    totals[category] = totals[category] + amount
                else:
                    totals[category] = amount

        for c in totals:
            print(c, ":", totals[c])

    # 3. Monthly report
    elif choice == "3":
        month = input("Enter month (YYYY-MM): ")
        total = 0

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["date"].startswith(month):
                    total = total + float(row["amount"])

        print("Total expense for", month, ":", total)

    # 4. Exit
    elif choice == "4":
        print("Program ended")
        break
    else:
        print("Invalid choice")