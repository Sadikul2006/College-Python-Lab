# 27. Write a Python program to swap two elements in a list.
num = [10, 20, 30, 40, 50, 100, 200]
print("After swap: ", num)

pos1 = int(input("Enter first position: "))
pos2 = int(input("Enter second position: "))

num[pos1-1], num[pos2-1] = num[pos2-1], num[pos1-1]
print("Before swap: ", num)