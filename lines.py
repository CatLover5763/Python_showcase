import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        num = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip().startswith("#"):
                    continue
                elif line.strip() == "":
                    continue
                else:
                    num+=1
        print(num)
    except FileNotFoundError:
        sys.exit("File does not exist")
