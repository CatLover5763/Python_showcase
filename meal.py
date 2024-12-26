def main():
    x = input("What time is it? ")
    if 7 <= convert(x) <= 8:
        print("breakfast time")
    elif 12 <= convert(x) <= 13:
        print("lunch time")
    elif 18 <= convert(x) <= 19:
        print("dinner time")

def convert(time):
    Add = 0
    if "a.m." in time:
        time = time.removesuffix(" a.m.")
    elif "p.m." in time:
        time = time.removesuffix(" p.m.")
        Add = 1
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    time = float(hours + minutes)
    if Add == 1:
        time += 12
    return time

if __name__ == "__main__":
    main()
