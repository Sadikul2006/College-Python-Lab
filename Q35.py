# 35. Write a Python program to print positive numbers in a list.

n = int(input("Enter number of elements: "))
my_list = []
positive_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

for i in range(n):
    if my_list[i] > 0:
        positive_list.append(my_list[i])

print("List:", my_list)
print("Positive number in list:", positive_list)