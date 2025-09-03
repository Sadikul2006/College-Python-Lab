#Q.4 Write a Python program for simple interest.
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate interest: "))
t = float(input("Enter the time(in year): "))
simple_interest = (p * r * t) / 100
print("Simple Interest is:", simple_interest)