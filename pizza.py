import sys
import csv
from tabulate import tabulate

menu =[]

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            if sys.argv[1] == "regular.csv":
                for row in reader:
                    menu.append([row["Regular Pizza"], row["Small"], row["Large"]])
                print(tabulate(menu, headers=["Regular Pizza","Small", "Large"], tablefmt="grid"))
            if sys.argv[1] == "sicilian.csv":
                for row in reader:
                    menu.append([row["Sicilian Pizza"], row["Small"], row["Large"]])
                print(tabulate(menu, headers=["Sicilian Pizza","Small", "Large"], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
