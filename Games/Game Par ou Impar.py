import random
tot=''
cont=0
c1=random.randint(0,50)
print('-----JOGO-DO-PAR-OU-IMPAR-----')
while True:
    vj=int(input('Digite o valor a ser Jogado:'))
    print('-'*30)
    jp=str(input('Par ou Impar: (P/I)')).upper().strip()
    print('-'*30)
    soma=c1+vj
    r=soma%2
    if r==0:
        tot='PAR'
    if r!=0:
        tot='IMPAR'
    if r==0:
        if jp=='P':
            print('Jogador VENCEU!')
            cont+=1
        else:
            print('Jogador PERDEU!')
            print(f'Jogador jogou {vj}!')
            print(f'Computador jogou {c1}!')
            print(f'O total é {soma} e deu {tot}!')
            print('-' * 30)
            break
    if r!=0:
        if jp=='I':
            print('Jogador VENCEU!')
            cont+=1
        else:
            print('Jogador PERDEU!')
            print('-' * 30)
            print(f'Jogador jogou {vj}!')
            print(f'Computador jogou {c1}!')
            print(f'O total é {soma} e deu {tot}!')
            print('-'*30)
            break
    print('-'*30)
    print(f'Jogador jogou {vj}!')
    print(f'Computador jogou {c1}!')
    print(f'O total é {soma} e deu {tot}!')
    print('-'*30)
    print('QUANTAS VEZES VOCÊ CONSEGUE GANHAR?')
    print('-' * 30)
print('GAME OVER!!')
print('-' * 30)
print(f'Seu Total de vitórias foi {cont}!')
print('-' * 30)