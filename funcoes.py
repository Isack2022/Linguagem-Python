# Definindo funções em python
# Para criar funções em python,você deve usar o comando def(definiton)
# seguido do nome da funções e o paranteses, que pode ter ou não argumentos
# Em Python não é necessário definir o tipo de retorno

def soma(valores):
    x = 0
    for i in valores:
        x = x + i
    return x 

def media(valores):
    x =0
    for i in valores:
        x = x + i 
    return x / len(valores)

def maior (valores):
    x = valores[0]
    for i in range(1,len(valores)):
        if(i > x ):
            x = i
    return x