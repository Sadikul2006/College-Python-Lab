#Q.11 Write a Python program to find the factors of a Number:

n = int(input("Enter the number to find factors : "))

for i in range(1, n+1) :
    if n % i == 0 :
        print(i ," ")