rom random import randint

# создание и вывод массива

n = int(input('Введите размер массива '))
array=[0]*n
for i in range(n):
    array[i]=randint(0,20)
print(array) 

# поиск искомого числа

num=int(input('Введите число '))
number = len([item for item in array if item == num])
print ('искомое число:',num, ' массив:',array,'количество чисел в массиве:', number )
