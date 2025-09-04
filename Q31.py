# 31. Write a Python program to find smallest number in a list.

import sys
smallest = sys.maxsize
n = int(input("Enter number of elements: "))
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
    smallest = min(smallest, element)

print("List:",my_list)
print("Smallest elements in list:", smallest)