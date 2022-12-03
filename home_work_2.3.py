# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной идексах.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def sumOddElements(f_mylist: list):
    sum = 0
    for i in range(len(f_mylist)):
        if i % 2 == 1:
            sum += f_mylist[i]
    return sum

mylist = [2, 3, 5, 9, 3]
print('сумма элементов с нечетными индексами:',sumOddElements(mylist))