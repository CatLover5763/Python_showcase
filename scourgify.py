import sys
import csv

data = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    sys.exit(f"Could not read {sys.argv[1]}")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = (row["name"].split(","))
                data.append({"first": name[1].strip(), "last": name[0].strip(), "house": row["house"]})
        with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for _ in data:
                    writer.writerow(_)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
