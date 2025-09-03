# 18. Write a Python program to find sum of natural numbers using recursion.
def sumN(n) :
    if n == 1:
        return 1
    else:
        return n + sumN(n-1)

n = int(input("Enter the value of n: "))
print(f"Sum of first {n} natural numbers is:", sumN(n))