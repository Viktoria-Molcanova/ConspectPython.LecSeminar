#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь 
#в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

# создание и вывод массива

n = int(input('Введите размер массива: '))
list=[0] * n
for i in range(n):
    list[i]=randint(0,20)
print(list) 
val = int(input('Введите число:  '))

# расчёт ближайшего элемента

min = max(list) - val
closest_num = -1
for i in list:
    if abs(i - val) < min:
        min = abs(i - val)
        closest_num = i

 # печать результата       

print('В массиве ',list,'ближайший элемент к заданному числу ', val, 'является ', closest_num)  
