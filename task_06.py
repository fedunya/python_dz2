# Напишите программу, которая принимает на вход вещественное число и
#  показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
os.system("cls")
num = input('Введите число: ')
sum = 0
for i in num:
    if i.isdigit():
        sum += int(i)
print("Сумма цифр: ", sum)
