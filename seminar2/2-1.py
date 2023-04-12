
from random import randint
count=int(input('Введите количество монет: '))
array=[0]*count
for i in range(count):
    array[i]=randint(0,1)
print(array) 


orel = len([item for item in array if item != 0])
reshka = len([item for item in array if item == 0])

if orel > reshka:
    print('Нужно перевернуть количество монет: ', reshka, '(с 0 на 1) ')

else:
    print('Нужно перевернутьколичество монет',orel, ' (с 1 на 0) ')



