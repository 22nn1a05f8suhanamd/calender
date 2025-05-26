# 0 -6 : for sunday to saturday
year = int (input("Enter a year: "))
leap = (year - 1) // 4 + (year - 1) // 400 - (year - 1) // 100
current_day = int (((year - 1) + 1 + leap) % 7)  # January 1 of given input year

for month in range(1, 13):
    if month == 1:
        days = 31
        print("\n\t January")
    elif month == 2:
        days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
        print("\n\t February")
    elif month == 3:
        days = 31
        print("\n\t March")
    elif month == 4:
        days = 30
        print("\n\t April")
    elif month == 5:
        days = 31
        print("\n\t May")
    elif month == 6:
        days = 30
        print("\n\t June")
    elif month == 7:
        days = 31
        print("\n\t July")
    elif month == 8:
        days = 31
        print("\n\t August")
    elif month == 9:
        days = 30
        print("\n\t September")
    elif month == 10:
        days = 31
        print("\n\t October")
    elif month == 11:
        days = 30
        print("\n\tNovember")
    elif month ==  12:
        days = 31
        print("\n\t December")
    current_day %= 7
    print("S  M  T  W  T  F  S")
    for i in range(0, current_day):
        print("  ", end=" ")
    for i in range(1, days + 1):
        if current_day == 7:
            print()
            current_day = 0
        if i < 10:
            print(f"{i}  ", end="")
        else:
            print(f"{i} ", end="")
        current_day += 1
    print("\n")

    
