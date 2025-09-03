# 17. Write a Python program for sum of squares of first n natural numbers.
num = int(input("Enter the value of n: "))
sum = 0
for i in range(1, num+1) :
    sum += i*i
print("Sum =", sum)