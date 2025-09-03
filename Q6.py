#Q.6 [i] Write a Python program to swap two variables using third variable.
a = 10
b = 20
temp = a
a = b
b = temp
print(f"a = {a} & b = {b}")

#Q.6 [ii] Write a Python program to swap two variables without using third variable.
a = 10
b = 20
a += b
b = a - b
a = a - b
print(f"a = {a} & b = {b}")