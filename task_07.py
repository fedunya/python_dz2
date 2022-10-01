# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system("cls")
list = []
num = input('Введите целое число больше нуля: ')
while not num.isdigit() or num == '0':
    print('Неверный ввод, повторите!')
    num = input('Введите целое число больше нуля: ')
num = int(num)
for i in range(1, num+1):
    multiply = 1
    for j in range(1, i+1):
        multiply *= j
    list.append(multiply)
print(list)

