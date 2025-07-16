#Write a program that takes a list of numbers and returns a new list with only even numbers doubled.

list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = []

for n in list_1:
    if n % 2 == 0:
        list_2.append(n*2)


print(list_2)

# DAY 1 TOO EASY