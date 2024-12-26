while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            date_list = date.split(sep="/")
            if  int(date_list[1]) > 31 or int(date_list[0]) > 12:
                pass
            else:
                print(f"{date_list[2]:02}-{int(date_list[0]):02}-{int(date_list[1]):02}")
                break
        elif "," in date:
            date = date.replace(',', '')
            date_list = date.split(sep=" ")
            match date_list[0]:
                case "January":
                    date_list[0] = 1
                case "February":
                    date_list[0] = 2
                case "March":
                    date_list[0] = 3
                case "April":
                    date_list[0] = 4
                case "May":
                    date_list[0] = 5
                case "June":
                    date_list[0] = 6
                case "July":
                    date_list[0] = 7
                case "August":
                    date_list[0] = 8
                case "September":
                    date_list[0] = 9
                case "October":
                    date_list[0] = 10
                case "November":
                    date_list[0] = 11
                case "December":
                    date_list[0] = 12
            if  int(date_list[1]) > 31 or int(date_list[0]) > 12:
                pass
            else:
                print(f"{date_list[2]:02}-{int(date_list[0]):02}-{int(date_list[1]):02}")
                break
        else:
            pass
    except ValueError:
        pass
