a=input('Введите фразу стихотворения: ')
count=0
glanye=set("аеёиоуэюя")
for letter in a:
    if letter in glanye:
        count +=1
print("Количество гласных",count)
if count//2==0 :
    print("парам пам-пам")
else:
    print("пам парам")
