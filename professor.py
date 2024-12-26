import random

number_list = []
score = 0
wrong = 0

def main():
    global score
    global number_list
    global wrong
    level_input = get_level()
    for k in range(1, 11):
        generate_integer(level_input)
        answer = int(input(f"{number_list[0]} + {number_list[1]} = "))
        while True:
            if number_list[0] + number_list[1] == answer:
                score +=1
                break
            else:
                print("EEE")
                wrong += 1
                if wrong == 3:
                    print(f"{number_list[0]} + {number_list[1]} = {number_list[0] + number_list[1]}")
                    break
                else:
                    answer = int(input(f"{number_list[0]} + {number_list[1]} = "))
        number_list = []
        wrong = 0
    print(f"Score: {score}")

def get_level():
    while True:
        level_input = input("Level: ")
        if level_input in ["1", "2", "3"]:
            return int(level_input)

def generate_integer(level):
    if level == 1:
        rand_number = random.randint(0, 9)
        number_list.append(rand_number)
        rand_number = random.randint(0, 9)
        number_list.append(rand_number)
    elif level == 2:
        rand_number = random.randint(10, 99)
        number_list.append(rand_number)
        rand_number = random.randint(10, 99)
        number_list.append(rand_number)
    elif level == 3:
        rand_number = random.randint(100, 999)
        number_list.append(rand_number)
        rand_number = random.randint(100, 999)
        number_list.append(rand_number)

if __name__ == "__main__":
    main()
