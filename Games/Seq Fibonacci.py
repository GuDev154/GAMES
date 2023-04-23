print('-------SEQUÊNCIA DE FIBONACCI--------')
nt=int(input('Digite a quantidade de termos:'))
cont=3
n1=0
n2=1
print('-'*37)
print('{}..'.format(n1))
print('{}..'.format(n2))
while cont<=nt:
    n3=n1+n2
    print('{}..'.format(n3))
    n1=n2
    n2=n3
    cont += 1
print('-'*37)
print('=+'*8,'FIM','=+'*8)
print('-'*37)
