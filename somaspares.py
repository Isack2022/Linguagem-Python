lista1 = [2,11,3,6,4,17,10]
lista2 = [1,2,3,6,12,20,8,22]

yu = 0
#Exibir os números pares da lista 1 e 2
for x in lista1:
    if (x % 2 == 0):
        yu = yu + x
        

for y in lista2:
    if (y % 2 == 0):
        print(y)
        yu = yu + y

#Somar os números pares
print(yu)

    