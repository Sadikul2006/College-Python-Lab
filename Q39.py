# 39. Write a Python program to find Cumulative sum of a list.

n = int(input("Enter the number of element in list: "))
number_list = []
cumulative_list = []
for i in range(n) :
    val = int(input(f"Enter the elwment in position {i+1}: "))
    number_list.append(val)

sum = 0
for i in range(n) :
    sum += number_list[i]
    cumulative_list.append(sum)

print("Orignal list:", number_list)
print("Cumulative_list:", cumulative_list)