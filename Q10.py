#Q.10 Write a Python program to find the largest among three numbers
a = int(input("Enter the first Numner: "))
b = int(input("Enter the second Numner: "))
c = int(input("Enter the third Numner: "))

if a > b and a > c :
    print("Largist Number is :", a)
elif b > c :
    print("Largist Number is :", b)
else :
    print("Largist Number is :", c)