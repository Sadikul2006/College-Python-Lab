# 19. Write a Python program to display Fibonacci sequence using recursion. Recursive function to return nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

n = int(input("Enter how many terms you want: "))
print("Fibonacci sequence:")

for i in range(n):
    print(fibonacci(i), end=" ")