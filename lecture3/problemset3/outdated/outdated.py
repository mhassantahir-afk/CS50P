# list for the months in a year
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# loop runs until valid input in entered
while True:
    try:
        date = input("Date: ")
        # if to check first type of input
        if "/" in date:
            date = date.strip(" ")
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if month <= 12 and day <= 31:
                print(year, f"{month:02}", f"{day:02}", sep="-")
                break
        # else for second type of input
        else:
            month, day, year = date.split(" ")
            month = int(months.index(month))+1
            if day.endswith(","):
                day = int(day.removesuffix(","))
                if day<= 31:
                    print(year, f"{month:02}", f"{day:02}", sep="-")
                    break
    except(ValueError):
        continue
