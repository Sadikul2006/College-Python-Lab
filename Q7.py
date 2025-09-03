#Q.7 Write a Python program to check if a number is positive, negative or 0.
num = int(input("Enter the number: "))
if num > 0 :
    print(f"{num} is a positive number.")
elif num < 0 :
    print(f"{num} is a negative number.")
else : 
    print("Number is a 0")