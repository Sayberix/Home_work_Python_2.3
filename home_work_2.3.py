# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# функция правильного математического округления до целого числа
def int_round(num: float) -> int:
    if int(num * 10) % 10 > 4:
        return int(num + 1)
    else:
        return int(num)

def multiplication_pairs(f_my_list: list)  -> list[int]:
    resault = []
    range_list = int_round(len(f_my_list)/2)
    #range_list = int_round(2.4)
    for i in range(int(range_list)):
        resault.append(f_my_list[i] * f_my_list[int(range_list) + 1 - i])
    return resault

my_list = [2, 3, 5, 6]
print('результат:',multiplication_pairs(my_list))