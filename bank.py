greet = input("Greeting: ").lower()

if "hello" in greet:
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")
