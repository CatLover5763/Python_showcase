def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  len(s) < 2 or len(s) > 6 or "." in s or " " in s:
        return False
    elif s[0].isdecimal() or s[1].isdecimal():
        return False
    number = 0
    letter = -2 #the first two character will always be letter
    for i in range(len(s)):
        if s[i].isdecimal():
            number = number + 1
            if number == 1 and int(s[i]) == 0:
                return False
        elif s[i].isalpha():
            letter = letter + 1
            if number > 0 and letter >= 1:
                return False
    else:
        return True


if __name__ == "__main__":
    main()
