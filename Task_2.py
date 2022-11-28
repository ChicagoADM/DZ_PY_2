# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
import os
clear = lambda: os.system('cls')
clear()
number = int(input('Введите число N: '))
num = 1
arr = []
for i in range(1, number + 1):
    num = num * i
    arr.append(num)

print(f'Произведения чисел{arr}')

input('Нажмите Enter для выхода ...')