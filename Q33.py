# 33. Write a Python program to print even numbers in a list.

n = int(input("Enter number of elements: "))
my_list = []
even_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

for i in range(n):
    if my_list[i] % 2 == 0:
        even_list.append(my_list[i])

print("List:", my_list)
print("Even number in list:", even_list)