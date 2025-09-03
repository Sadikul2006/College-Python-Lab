#Q.8 Write a Python program to check if a number is odd or even.
num = int(input("Enter the number check odd or even: "))
if num == 0 :
    print("Number is 0")
elif num % 2 == 0 :
    print(f"{num} is a even Number.")
else :
    print(f"{num} is a odd Number.")