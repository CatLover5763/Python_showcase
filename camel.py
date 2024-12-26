def spiltupper(x):
    spilt_camelcase = ""
    for i in range(len(x)):
        if x[i].islower():
            spilt_camelcase = spilt_camelcase + x[i]
        elif x[i].isupper():
            spilt_camelcase = spilt_camelcase + "-"
            spilt_camelcase = spilt_camelcase + x[i].lower()
    spilt_camelcase = spilt_camelcase.split("-")
    x = spilt_camelcase
    return x

camelcase = input("camelCase: ")
snakecase = spiltupper(camelcase)

for i in range(len(snakecase)):
    print(snakecase[i], end="")
    if i + 1 < len(snakecase):
        print("_", end="")
print("")
