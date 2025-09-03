# Q.15 Write a Python program to print all Prime numbers in an interval.
import math

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

for i in range(start, end + 1):
    if i < 2:
        continue

    is_prime = True
    root = int(math.sqrt(i)) + 1

    for j in range(2, root):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
