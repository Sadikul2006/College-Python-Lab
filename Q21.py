#Q.21 Write a Python program to find sum of array.

n = int(input("Enter the size of array: "))
arr = []
sum = 0
for i in range(n):
    value = int(input(f"Enter the value of index {i}: "))
    arr.append(value)
    sum += value

print("Array elements are:", arr)
print("Sum of an array elements:", sum)