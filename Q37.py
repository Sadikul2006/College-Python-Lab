# 37. Write a Python program Cloning or Copying a list.

n = int(input("Enter number of elements: "))
original_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    original_list.append(element)

cloned_list = original_list[:]

print("Original List:", original_list)
print("Cloned List:", cloned_list)