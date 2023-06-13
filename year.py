year = int(input("Enter the year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and year > 2023:
        print(year, "will be a leap year")
elif (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and year < 2023:
        print(year, "was a leap year")
elif (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and year == 2023:
        print(year, "is not a leap year")
elif (year % 4 != 0 and (year % 100 == 0 or year % 400 != 0)) and year > 2023:
        print(year, "will not be a leap year")
elif (year % 4 != 0 and (year % 100 == 0 or year % 400 != 0)) and year < 2023:
        print(year, "was not a leap year")


