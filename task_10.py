# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# -> [0,1,2, 3,4, 5, 6,7,8, 9]
# -> [0, 7, 6, 3,4, 2, 9, 5,1,8]

import os, random
os.system("cls")
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Исходный список -> {list}')
for i in range(len(list)):
    index_rand = random.randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[index_rand]
    list[index_rand] = temp
print(f'Перемешанный список -> {list}')
