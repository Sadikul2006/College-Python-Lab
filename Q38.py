# 38. Write a Python program to count occurrences of an element in a list.

n = int(input("Enter number of elements: "))
number_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    number_list.append(element)

print("List:", number_list)

num = int(input("Enter the number to find occurrences count: "))
count = number_list.count(num)
print(f"Occurrences of {num} is: {count}")