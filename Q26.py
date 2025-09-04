# 26. Write a Python program to interchange first and last elements in a list.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(num)
num[0], num[n-1] = num[n-1], num[0]
print(num)