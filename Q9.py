#Q.9 Write a Python program to check leap year.
year = int(input("Enter the year: "))
if year % 4 == 0 :
    print(f"{year} is a leap year")
else :
    print(f"{year} is a not leap year")