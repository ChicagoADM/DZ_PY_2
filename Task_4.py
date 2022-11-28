# Реализуйте алгоритм перемешивания списка.
import os
clear = lambda: os.system('cls')
clear()
import random

list = list(range(0,10))
print(list)
for i in range(len(list)):
    j = random.randrange(0, i + 1)
    list[i] , list[j] = list[j], list[i]
print(list)
print()
input('Нажмите Enter для выхода ...')