# 20. Write a Python program to find Factorial of number using recursion.

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter the factorial Number: "))    
print(f"{n}! = {factorial(n)}")
