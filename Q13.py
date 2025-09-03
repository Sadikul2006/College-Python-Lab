# Q.13 Write a Python program to check Armstrong number.

num = int(input("Enter the number chack Armstrong or not: "))
length = len(str(num))
temp = num
sum = 0
while temp > 0 :
    digit = temp % 10
    sum += (digit**length)
    temp = int(temp/10)
if sum == num :
    print(num, "is a Armstrong number") 
else :
    print(num, "is a not Armstrong number")

