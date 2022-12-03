# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def conversion_binary(f_number: int) -> str:
    resault = ''
    while f_number != 0:
        if f_number % 2 == 0:
            f_number /= 2
            resault += '0'
        else:
            f_number = (f_number - 1) / 2
            resault += '1'
    return resault

number = int(input('введите число в десятичной системе: '))
print('число -',number,'в двоичной системе равно:',conversion_binary(number))