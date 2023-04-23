n1=int(input('Primeiro Termo:'))
r=int(input('Razão:'))
t=n1
cont=1
mais=10
total=0
while mais !=0:
     total += mais
     while cont<total:
         print('{} -> '.format(t),end='')
         t += r
         cont+=1
     print('PAUSA')
     print('Para Sair Digite 0!')
     mais = int(input('Quantos termos quer mostrar a mais:'))
print('FIM DA P.A')