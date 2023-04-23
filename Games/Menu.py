from time import sleep
op=0
n1=int(input('Digite o 1° número:'))
n2=int(input('Digite o 2° número:'))
print('--------MENU DE OPÇÕES--------')
print('Escolha o que deseja fazer:')
while op!=4:
    print('[ 1 ] - SOMAR')
    print('[ 2 ] - MULTIPLICAR')
    print('[ 3 ] - NEW NUMBERS')
    print('[ 4 ] - FECHAR MENU')
    op=int(input('Digite sua opção:'))
    print('-' * 30)
    if op==1:
        soma=n1+n2
        print('A soma entre {} e {} é {}!'.format(n1,n2,soma))
        print('-'*30)
    if op==2:
        mult=n1*n2
        print('A multiplicação entre {} e {} é {}!'.format(n1,n2,mult))
        print('-' * 30)
    if op==3:
        n1 = int(input('Digite o 1° número:'))
        n2 = int(input('Digite o 2° número:'))
        print('-' * 30)
    if op==4:
        print('Encerando...')
        sleep(1)
        print('Fim do PROGRAMA!')
        print('-' * 30)
    if op!=1 and op !=2 and op !=3 and op !=4:
         print('OPÇÃO INVALIDA!!')
         print('-' * 30)

