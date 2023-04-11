listinha = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


#Código para lista de 1 a 9
print("Lista de 1 a 9: ") 
for d in range(1,10):
    print(listinha[d])

#Código para lista de 8 a 13
print("\nLista de 8 a 13: ")
for q in range(8,14):
    print(listinha[q])

#Código para ver os números pares e ímpares da lista
print("\nLista para ver os números pares e ímpares")
for x in listinha:
    if (x % 2 == 0):
        print("Número par: " + str(x))
    else:
        print("Número ímpar: " + str(x))

#Código para ver os números mútiiplos de 2
print("\nOs números para ver os mútiplos de 2")
for y in listinha:
    if (y % 2 ==0):
        print("Mútiplo de 2: " + str(y))

#Código para ver os números mútiiplos de 3
print("\nOs números para ver os mútiplos de 3")
for n in listinha:
    if(n % 3 ==0):
        print("Mútiplo de 3: " + str(n))

#Código para ver os números mútiiplos de 4
print("\nOs números para ver os mútiplos de 4")
for n in listinha:
    if(n % 4 ==0):
        print("Mútiplo de 4: " + str(n))

#Código para reverter a lista 
z = listinha[::-1]
print("\nLista reversa:")
print(z)




