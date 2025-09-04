# Q.22 Write a Python program to find largest element in an array

n = int(input("Enter the size of array: "))
arr = []
largest = float('-inf')
for i in range(n) :
    value = int(input(f"Enter the value of index {i}: "))
    arr.append(value)
    largest = max(largest, value)

print("Array elements are: ", arr)
print("largest element in array: ", largest)