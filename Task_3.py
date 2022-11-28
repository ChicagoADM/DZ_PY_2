# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
import os
clear = lambda: os.system('cls')
clear()
n = int(input('Введите число: '))
sum = 0
arr = []
for i in range(1, n + 1):
    num = round((1 + 1 / i)**i, 2)
    arr.append(num)
    sum += num
print(f'Список чисел последовательности {arr} \nСумма последовательности чисел: {sum}')

input('Нажмите Enter для выхода ...')