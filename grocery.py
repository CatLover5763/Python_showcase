grocery_list = {}

while True:
    try:
        item = input()
        if item not in grocery_list:
            grocery_list.setdefault(item, 1)
        elif item in grocery_list:
            grocery_list[item] += 1
    except EOFError:
        grocery_list = dict(sorted(grocery_list.items()))
        for i in grocery_list:
            print(grocery_list[i], i.upper())
        break
