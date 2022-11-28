# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import os
clear = lambda: os.system('cls')
clear()
num = float(input('Введите число '))
num = str(num)
sum = 0
for i in range(len(num)):
    if num[i] != ".":
        sum += int(num[i])

print(f'Сумма цифр {sum}')

input('Нажмите Enter для выхода ...')