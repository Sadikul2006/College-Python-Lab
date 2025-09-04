# 24. Write a Python program to multiply two matrices.

def create(matrix, r, c):
    for i in range(r):
        row = []
        for j in range(c):
            val = int(input(f"Enter data for [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)

def display(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

def multiply(matrix1, matrix2):
    c1 = len(matrix1[0])
    r2 = len(matrix2)
    
    if c1 != r2:
        print("Multiply not possible!")
        return None, None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result


matrix1 = []
rows = int(input("Enter the number of rows in first matrix: "))
cols = int(input("Enter the number of columns in first matrix: "))
create(matrix1, rows, cols)
print("First matrix:")
display(matrix1)

matrix2 = []
rows = int(input("Enter the number of rows in second matrix: "))
cols = int(input("Enter the number of columns in second matrix: "))
create(matrix2, rows, cols)
print("Second matrix:")
display(matrix2)

result = multiply(matrix1, matrix2)
if result:
    print("Result matrix:")
    display(result)