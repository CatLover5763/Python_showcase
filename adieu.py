import inflect
p = inflect.engine()

try:
    name_list = []
    while True:
        name = input("Name: ")
        name_list.append(name)
except EOFError:
    print(f"Adieu, adieu, to {p.join(name_list)}")
