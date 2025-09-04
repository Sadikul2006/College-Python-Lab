# 32. Write a Python program to find largest number in a list.

import sys
largest = -sys.maxsize
n = int(input("Enter number of elements: "))
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
    largest = max(largest, element)

print("List:",my_list)
print("Largest elements in list:", largest)