def is_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False

year=int(input("Enter a year to check if it is a leap year: "))

if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")