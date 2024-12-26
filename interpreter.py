math = input("Expression: ")
x, y, z = math.split()
x = float(x)
z = float(z)

if y == "+":
    math = x + z
elif y == "-":
    math = x - z
elif y == "*":
    math = x * z
else:
    math = x / z

print(math)
