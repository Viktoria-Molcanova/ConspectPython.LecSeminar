##Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
##Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

##Вариант 1

from random import randint
count=2
array=[0]*count

for i in range(count):
    array[i]=randint(1,1000)
print(array, array[0] + array[1], array[0] * array[1]) 

##Вариант 2

x = int(input("Введите x: "))
y = int(input("Введите y: "))

for i in range(x):
    for j in range(y):
  
        if x == i + j and y == i * j:
            print(i, j)
