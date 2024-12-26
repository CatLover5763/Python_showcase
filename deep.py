answer = input(" What is the Answer to the Great Question of Life, the Universe and Everything ").lower().replace("-", " ").lstrip().rstrip()

#print(f'"{answer}"')

match answer:
    case "42" | "forty two" :
        print("Yes")
    case _:
        print("No")
