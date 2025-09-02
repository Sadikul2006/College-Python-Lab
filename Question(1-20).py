# Q.1 Write a Python program to add two numbers.
# num1  = int(input("Enter the first number: "))
# num2  = int(input("Enter the second number: "))
# result = num1 + num2
# print("The sum is:", result)


# Q.2 Write a Python program to find maximum of two numbers.
# num1  = int(input("Enter the first number: "))
# num2  = int(input("Enter the second number: "))
# if num1 > num2:
#     print("The maximum number is:", num1)
# elif num2 > num1:
#     print("The maximum number is:", num2)
# else :
#     print("Both number are eqal.")


# Q.3 Write a Python program for factorial of a number.
# num = int(input("Enter the factorial of a number: "))
# fac = 1
# for i in range(1, num+1):
#     fac *= i
# print(f"The {num}! is {fac}")


# Q.4 Write a Python program for simple interest.
# p = float(input("Enter the principle amount: "))
# r = float(input("Enter the rate interest: "))
# t = float(input("Enter the time(in year): "))
# simple_interest = (p * r * t) / 100
# print("Simple Interest is:", simple_interest)


# Q.5 Write a Python program for compound interest.
# p = float(input("Enter the principle amount: "))
# r = float(input("Enter the rate interest: "))
# t = float(input("Enter the time(in year): "))
# a = p * (1 + (r/100))**t
# compound_interest = a - p
# print(f"The Compound Interest is: {compound_interest:.2f}")


# Q.6 [i] Write a Python program to swap two variables using third variable.
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print(f"a = {a} & b = {b}")

# Q.6 [ii] Write a Python program to swap two variables without using third variable.
# a = 10
# b = 20
# a += b
# b = a - b
# a = a - b
# print(f"a = {a} & b = {b}")


# Q.7 Write a Python program to check if a number is positive, negative or 0.
# num = int(input("Enter the number: "))
# if num > 0 :
#     print(f"{num} is a positive number.")
# elif num < 0 :
#     print(f"{num} is a negative number.")
# else : 
#     print("Number is a 0")


# Q.8 Write a Python program to check if a number is odd or even.
# num = int(input("Enter the number check odd or even: "))
# if num == 0 :
#     print("Number is 0")
# elif num % 2 == 0 :
#     print(f"{num} is a even Number.")
# else :
#     print(f"{num} is a odd Number.")

# Q.9 Write a Python program to check leap year.
# year = int(input("Enter the year: "))
# if year % 4 == 0 :
#     print(f"{year} is a leap year")
# else :
#     print(f"{year} is a not leap year")


# Q.10 Write a Python program to find the largest among three numbers

# a = int(input("Enter the first Numner: "))
# b = int(input("Enter the second Numner: "))
# c = int(input("Enter the third Numner: "))

# if a > b and a > c :
#     print("Largist Number is :", a)
# elif b > c :
#     print("Largist Number is :", b)
# else :
#     print("Largist Number is :", c)


# Q.11 Write a Python program to find the factors of a Number:

# n = int(input("Enter the number to find factors : "))

# for i in range(1, n+1) :
#     if n % i == 0 :
#         print(i ," ")


#Q.12 Write a Python program to make a simple calculator.

# def add(x, y):
#     return x+y

# def subtract(x, y):
#     return x-y

# def multiply(x, y):
#     return x*y

# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero!"
#     return x/y

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1' :
#     print("Ans:",add(num1, num2))
# elif choice == '2' :
#     print("Ans:",subtract(num1, num2))
# elif choice == '3' :
#     print("Ans:",multiply(num1, num2))
# elif choice == '4' :
#     print("Ans:",divide(num1, num2))
# else :
#     print("invalid input!")


# Q.13 Write a Python program to check Armstrong number.

# num = int(input("Enter the number chack Armstrong or not: "))
# length = len(str(num))
# temp = num
# sum = 0
# while temp > 0 :
#     digit = temp % 10
#     sum += (digit**length)
#     temp = int(temp/10)
# if sum == num :
#     print(num, "is a Armstrong number") 
# else :
#     print(num, "is a not Armstrong number")

# Q.14 Write a Python program to find area of a circle.
# redius = float(input("Enter Radius of a circle: "))
# pi = 3.14
# area = pi * redius * redius
# print("Area of circle : ", area)


# Q.15 Write a Python program to print all Prime numbers in an interval.
# import math

# start = int(input("Enter the start of the interval: "))
# end = int(input("Enter the end of the interval: "))

# for i in range(start, end + 1):
#     if i < 2:
#         continue

#     is_prime = True
#     root = int(math.sqrt(i)) + 1

#     for j in range(2, root):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(i)


# 16. Write a Python program for nth Fibonacci number.

# a = 0
# b = 1
# temp = -1
# n = int(input("Enter the position find fibonacci Number: "))
# if n == 1:
#     temp = a
# if n == 2:
#     temp = b
# for i in range(3, n+1) :
#     temp = a + b
#     a = b
#     b = temp
# if temp != -1 :
#     print(temp)
# else:
#     print("Invalid Position!.")


    
# 17. Write a Python program for sum of squares of first n natural numbers.

# num = int(input("Enter the value of n: "))
# sum = 0
# for i in range(1, num+1) :
#     sum += i*i
# print("Sum =", sum)


# 18. Write a Python program to find sum of natural numbers using recursion.
# def sumN(n) :
#     if n == 1:
#         return 1
#     else:
#         return n + sumN(n-1)

# n = int(input("Enter the value of n: "))
# print(f"Sum of first {n} natural numbers is:", sumN(n))


# 19. Write a Python program to display Fibonacci sequence using recursion.

# Recursive function to return nth Fibonacci number
# def fibonacci(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1 
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2) 

# n = int(input("Enter how many terms you want: "))
# print("Fibonacci sequence:")

# for i in range(n):
#     print(fibonacci(i), end=" ")



# 20. Write a Python program to find Factorial of number using recursion.

# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# n = int(input("Enter the factorial Number: "))    
# print(f"{n}! = {factorial(n)}")
