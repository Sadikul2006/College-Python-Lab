#Q.3 Write a Python program for factorial of a number.
num = int(input("Enter the factorial of a number: "))
fac = 1
for i in range(1, num+1):
    fac *= i
print(f"The {num}! is {fac}")