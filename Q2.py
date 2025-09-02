# Q.2 Write a Python program to find maximum of two numbers.
num1  = int(input("Enter the first number: "))
num2  = int(input("Enter the second number: "))
if num1 > num2:
    print("The maximum number is:", num1)
elif num2 > num1:
    print("The maximum number is:", num2)
else :
    print("Both number are eqal.")