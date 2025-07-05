year = int(input("Enter the year : "))

if (year % 4 == 0 and year % 100 != 100) and (year % 400 == 0):
    print(f"Given year {year} is a leap Year")
else:
    print(f"Given year {year} is not a leap Year")