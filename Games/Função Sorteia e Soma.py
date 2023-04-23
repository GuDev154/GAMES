import random


def sortea(lista):
    for c in range(0,6):
     n=random.randint(0,10)
     lista.append(n)
     c+=1


def par(lista):
    soma=0
    for v in lista:
        if v %2 ==0:
          soma+=v
    print(f'A soma dos valores Pares é {soma}!')



numeros=list()
sortea(numeros)
print(numeros)
par(numeros)
