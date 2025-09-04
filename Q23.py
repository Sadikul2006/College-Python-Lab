# Q.23 Write a Python program to add two matrices

def create(matrix, rows, cols):
    for i in range(rows):
        current_row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i}][{j}]: "))
            current_row.append(value)
        matrix.append(current_row)


def display(matrix):
    for row in matrix:
        print(row)


def add(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    for i in range(rows):
        current_row = []
        for j in range(cols):
            current_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(current_row)


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = []
matrix2 = []
result = []

print("First Matrix:")
create(matrix1, rows, cols)

print("Second Matrix:")
create(matrix2, rows, cols)

add(matrix1, matrix2)

print("\nFirst Matrix:")
display(matrix1)

print("Second Matrix:")
display(matrix2)

print("Sum of two Matrices:")
display(result)
