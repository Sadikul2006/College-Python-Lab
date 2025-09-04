# 29. Write a Python program reversing a List.
n = int(input("Enter the number of element in list : "))
list = []
for i in range(n):
    val = int(input(f"Enter element in position {i+1}: "))
    list.append(val)

list.reverse()

print(list)