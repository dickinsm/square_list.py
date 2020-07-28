# Author: Makaliah Dickinson
# Date: 7/27/2020
# Description: Write a function that takes as a parameter a list of numbers and replaces each value with the square of
#             that value.

def square_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]


lst = [7, -3, 12, 9]
square_list(lst)
print(lst)
