# 34. Write a Python program to print all odd numbers in a range.

n = int(input("Enter number of elements: "))
my_list = []
odd_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

for i in range(n):
    if my_list[i] % 2 != 0:
        odd_list.append(my_list[i])

print("List:", my_list)
print("Odd number in list:", odd_list)