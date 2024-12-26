amount_due = 50

while True:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    #check if coin is usable
    if insert_coin != 5 and insert_coin != 10 and insert_coin != 25:
        insert_coin = 0
    amount_due = amount_due - insert_coin
    #if the money is enougn the loop will break
    if amount_due <= 0:
        print(f"Change Owed: {amount_due * -1}")
        break
