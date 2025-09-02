# Q.21 Write a Python program to find sum of array.

# n = int(input("Enter the size of array: "))
# arr = []
# sum = 0
# for i in range(n):
#     value = int(input(f"Enter the value of index {i}: "))
#     arr.append(value)
#     sum += value

# print("Array elements are:", arr)
# print("Sum of an array elements:", sum)



# Q.22 Write a Python program to find largest element in an array

# n = int(input("Enter the size of array: "))
# arr = []
# largest = float('-inf')
# for i in range(n) :
#     value = int(input(f"Enter the value of index {i}: "))
#     arr.append(value)
#     largest = max(largest, value)

# print("Array elements are: ", arr)
# print("largest element in array: ", largest)


# Q.23 Write a Python program to add two matrices

# def create(matrix, rows, cols):
#     for i in range(rows):
#         current_row = []
#         for j in range(cols):
#             value = int(input(f"Enter element [{i}][{j}]: "))
#             current_row.append(value)
#         matrix.append(current_row)


# def display(matrix):
#     for row in matrix:
#         print(row)


# def add(matrix1, matrix2):
#     rows = len(matrix1)
#     cols = len(matrix1[0])
#     for i in range(rows):
#         current_row = []
#         for j in range(cols):
#             current_row.append(matrix1[i][j] + matrix2[i][j])
#         result.append(current_row)


# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# matrix1 = []
# matrix2 = []
# result = []

# print("First Matrix:")
# create(matrix1, rows, cols)

# print("Second Matrix:")
# create(matrix2, rows, cols)

# add(matrix1, matrix2)

# print("\nFirst Matrix:")
# display(matrix1)

# print("Second Matrix:")
# display(matrix2)

# print("Sum of two Matrices:")
# display(result)



# 24. Write a Python program to multiply two matrices.

# def create(matrix, r, c):
#     for i in range(r):
#         row = []
#         for j in range(c):
#             val = int(input(f"Enter data for [{i}][{j}]: "))
#             row.append(val)
#         matrix.append(row)

# def display(matrix):
#     for row in matrix:
#         for val in row:
#             print(val, end=" ")
#         print()

# def multiply(matrix1, matrix2):
#     c1 = len(matrix1[0])
#     r2 = len(matrix2)
    
#     if c1 != r2:
#         print("Multiply not possible!")
#         return None, None
    
#     result = []
#     for i in range(len(matrix1)):
#         row = []
#         for j in range(len(matrix2[0])):
#             total = 0
#             for k in range(len(matrix2)):
#                 total += matrix1[i][k] * matrix2[k][j]
#             row.append(total)
#         result.append(row)
#     return result


# matrix1 = []
# rows = int(input("Enter the number of rows in first matrix: "))
# cols = int(input("Enter the number of columns in first matrix: "))
# create(matrix1, rows, cols)
# print("First matrix:")
# display(matrix1)

# matrix2 = []
# rows = int(input("Enter the number of rows in second matrix: "))
# cols = int(input("Enter the number of columns in second matrix: "))
# create(matrix2, rows, cols)
# print("Second matrix:")
# display(matrix2)

# result = multiply(matrix1, matrix2)
# if result:
#     print("Result matrix:")
#     display(result)


# 25. Write a Python program to transpose a matrix in single line.

# def display(matrix):
#     r = len(matrix)
#     c = len(matrix[0])
#     for i in range(r):
#         for j in range(c):
#             print(matrix[i][j], end=" ")
#         print()

# r = int(input("Enter the number of rows in matrix: "))
# c = int(input("Enter the number of columns in matrix: "))
# matrix = [] 
# for i in range(r) :
#     row = []
#     for j in range(c):
#         val = int(input(f"Enter data for matrix[{i}][{j}]: "))
#         row.append(val)
#     matrix.append(row)

# transpose = [[0 for _ in range(r)] for _ in range(c)]
# for i in range(c) :
#     for j in range(r):
#         transpose[i][j] = matrix[j][i]
        
# print("matrix: ")
# display(matrix)
# print("tanspose: ")
# display(transpose)


# 26. Write a Python program to interchange first and last elements in a list.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = len(num)
# num[0], num[n-1] = num[n-1], num[0]
# print(num)


# 27. Write a Python program to swap two elements in a list.
# num = [10, 20, 30, 40, 50, 100, 200]
# print("After swap: ", num)

# pos1 = int(input("Enter first position: "))
# pos2 = int(input("Enter second position: "))

# num[pos1-1], num[pos2-1] = num[pos2-1], num[pos1-1]
# print("Before swap: ", num)

     
# 28. Write a Python program to find length of list.
# list = [1, 2, 3, "apple", "mengo", 10.45, 23.99]
# length = len(list)
# print(length)


# 29. Write a Python program reversing a List.
# n = int(input("Enter the number of element in list : "))
# list = []
# for i in range(n):
#     val = int(input(f"Enter element in position {i+1}: "))
#     list.append(val)

# for i in range(n//2):
#     list[i], list[n-i-1] = list[n-i-1], list[i]

# print(list)


# 29. Write a Python program reversing a List.
# n = int(input("Enter the number of element in list : "))
# list = []
# for i in range(n):
#     val = int(input(f"Enter element in position {i+1}: "))
#     list.append(val)

# list.reverse()

# print(list)


# 30. Write a Python program to find sum of elements in list.

# n = int(input("Enter number of elements: "))
# list = []

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     list.append(element)

# total = sum(list)
# print("List:",list)
# print("Sum of elements in list:", total)


# 31. Write a Python program to find smallest number in a list.

# import sys
# smallest = sys.maxsize
# n = int(input("Enter number of elements: "))
# my_list = []
# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)
#     smallest = min(smallest, element)

# print("List:",my_list)
# print("Smallest elements in list:", smallest)


# 32. Write a Python program to find largest number in a list.

# import sys
# largest = -sys.maxsize
# n = int(input("Enter number of elements: "))
# my_list = []
# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)
#     largest = max(largest, element)

# print("List:",my_list)
# print("Largest elements in list:", largest)


# 33. Write a Python program to print even numbers in a list.

# n = int(input("Enter number of elements: "))
# my_list = []
# even_list = []

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)

# for i in range(n):
#     if my_list[i] % 2 == 0:
#         even_list.append(my_list[i])

# print("List:", my_list)
# print("Even number in list:", even_list)


# 34. Write a Python program to print all odd numbers in a range.

# n = int(input("Enter number of elements: "))
# my_list = []
# odd_list = []

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)

# for i in range(n):
#     if my_list[i] % 2 != 0:
#         odd_list.append(my_list[i])

# print("List:", my_list)
# print("Odd number in list:", odd_list)


# 35. Write a Python program to print positive numbers in a list.

# n = int(input("Enter number of elements: "))
# my_list = []
# positive_list = []

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)

# for i in range(n):
#     if my_list[i] > 0:
#         positive_list.append(my_list[i])

# print("List:", my_list)
# print("Positive number in list:", positive_list)


# 36. Write a Python program to print all negative numbers in a range.

# n = int(input("Enter number of elements: "))
# my_list = []
# negative_list = []

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)

# for i in range(n):
#     if my_list[i] < 0:
#         negative_list.append(my_list[i])

# print("List:", my_list)
# print("Negative number in list:", negative_list)





# 37. Write a Python program Cloning or Copying a list.

# n = int(input("Enter number of elements: "))
# original_list = []
# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     original_list.append(element)

# cloned_list = original_list[:]

# print("Original List:", original_list)
# print("Cloned List:", cloned_list)


# 38. Write a Python program to count occurrences of an element in a list.

# n = int(input("Enter number of elements: "))
# number_list = []

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     number_list.append(element)

# print("List:", number_list)

# num = int(input("Enter the number to find occurrences count: "))
# count = number_list.count(num)
# print(f"Occurrences of {num} is: {count}")


# 39. Write a Python program to find Cumulative sum of a list.

# n = int(input("Enter the number of element in list: "))
# number_list = []
# cumulative_list = []
# for i in range(n) :
#     val = int(input(f"Enter the elwment in position {i+1}: "))
#     number_list.append(val)

# sum = 0
# for i in range(n) :
#     sum += number_list[i]
#     cumulative_list.append(sum)

# print("Orignal list:", number_list)
# print("Cumulative_list:", cumulative_list)


# 40. Write a Python program to check if a string is palindrome or not.
# txt = input("Enter text to check palindrome or not: ")

# if txt == txt[::-1]:    # txt[-1:-(1+len(txt)):-1]
#     print(txt, "is a palindrome!")
# else:
#     print(txt, "is not a palindrome!")



