# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

import math as m

def find_diff(f_mylist: list) -> int:
    min, max = 1, 0
    for i in range(len(f_mylist)):
        number, _ = m.modf(f_mylist[i])
        number = round(number,len(str(f_mylist[i]).split('.')[1]))
        if number > max:
            max = number
        if number < min:
            min = number
    return max - min

my_list = [1.1, 1.2, 3.1, 10.01]
print(find_diff(my_list))
