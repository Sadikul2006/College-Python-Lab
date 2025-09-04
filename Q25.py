# 25. Write a Python program to transpose a matrix in single line.

def display(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print()

r = int(input("Enter the number of rows in matrix: "))
c = int(input("Enter the number of columns in matrix: "))
matrix = [] 
for i in range(r) :
    row = []
    for j in range(c):
        val = int(input(f"Enter data for matrix[{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

transpose = [[0 for _ in range(r)] for _ in range(c)]
for i in range(c) :
    for j in range(r):
        transpose[i][j] = matrix[j][i]
        
print("matrix: ")
display(matrix)
print("tanspose: ")
display(transpose)