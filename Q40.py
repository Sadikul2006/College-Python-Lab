# 40. Write a Python program to check if a string is palindrome or not.
txt = input("Enter text to check palindrome or not: ")

if txt == txt[::-1]:    # txt[-1:-(1+len(txt)):-1]
    print(txt, "is a palindrome!")
else:
    print(txt, "is not a palindrome!")