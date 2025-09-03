# 16. Write a Python program for nth Fibonacci number.
a = 0
b = 1
temp = -1
n = int(input("Enter the position find fibonacci Number: "))
if n == 1:
    temp = a
if n == 2:
    temp = b
for i in range(3, n+1) :
    temp = a + b
    a = b
    b = temp
if temp != -1 :
    print(temp)
else:
    print("Invalid Position!.")
