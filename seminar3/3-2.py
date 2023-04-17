from random import randint

# создание и вывод массива

n = int(input('Введите размер массива: '))
list=[0]*n
for i in range(n):
    list[i]=randint(0,20)
print(list) 
val = int(input('Введите число:  '))

# расчёт ближайшего элемента

min_d = max(list) - val
closest_num = -1
for i in list:
    if abs(i - val) < min_d:
        min_d = abs(i - val)
        closest_num = i

 # печать результата       

print('В массиве ',list,'ближайший элемент к заданному числу ', val, 'является ', closest_num)  

