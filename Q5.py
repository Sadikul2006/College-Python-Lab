#Q.5 Write a Python program for compound interest.
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate interest: "))
t = float(input("Enter the time(in year): "))
a = p * (1 + (r/100))**t
compound_interest = a - p
print(f"The Compound Interest is: {compound_interest:.2f}")