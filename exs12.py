year=int(input("Въведете година: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} е високосна година.")
else:
    print(f"{year} не е високосна година.")