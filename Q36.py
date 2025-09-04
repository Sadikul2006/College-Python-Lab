# 36. Write a Python program to print all negative numbers in a range.

n = int(input("Enter number of elements: "))
my_list = []
negative_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

for i in range(n):
    if my_list[i] < 0:
        negative_list.append(my_list[i])

print("List:", my_list)
print("Negative number in list:", negative_list)