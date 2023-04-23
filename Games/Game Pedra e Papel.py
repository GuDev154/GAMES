import random
from time import sleep
c=random.randint(0,2)
itens=('PEDRA','PAPEL','TESOURA')
print('\033[30m------------\033[0mJOKENPO\033[30m-------------')
print('\033[0mOpções:')
print('\033[37m[ 0 ] - PEDRA')
print('\033[37m[ 1 ] - PAPEL')
print('\033[37m[ 2 ] - TESOURA')
j=int(input('\033[0mQual sua Jogada:'))
print('\033[37mJO..')
sleep(0.5)
print('\033[37mKEN..')
sleep(0.5)
print('\033[37mPO!!')
print('\033[30m-'*30)
print('\033[37mJogador jogou {}'.format(itens[j]))
print('X')
print('\033[37mComputador jogou {}'.format(itens[c]))
#EMPATE:
if j==0 and c==0:
    print('\033[30m-' * 30)
    print('\033[33mEMPATE')
    print('\033[30m-' * 30)
elif j==1 and c==1:
    print('\033[30m-' * 30)
    print('\033[33mEMPATE')
    print('\033[30m-' * 30)
elif j==2 and c==2:
    print('\033[30m-' * 30)
    print('\033[33mEMPATE')
    print('\033[30m-' * 30)
#JOGADOR VENCE:
elif j==0 and c==2:
    print('\033[30m-' * 30)
    print('\033[32mJOGADOR VENCEU!!')
    print('\033[30m-' * 30)
elif j==1 and c==0:
    print('\033[30m-' * 30)
    print('\033[32mJOGADOR VENCEU!')
    print('\033[30m-' * 30)
elif j==2 and c==1:
    print('\033[30m-' * 30)
    print('\033[32mJOGADOR VENCEU!')
    print('\033[30m-' * 30)
#COMPUTADOR VENCE:
elif j==2 and c==0:
    print('\033[30m-' * 30)
    print('\033[31mCOMPUTADOR VENCEU!')
    print('\033[30m-' * 30)
elif j==0 and c==1:
    print('\033[30m-' * 30)
    print('\033[31mCOMPUTADOR VENCEU!')
    print('\033[30m-' * 30)
elif j==1 and c==2:
    print('\033[30m-' * 30)
    print('\033[31mCOMPUTADOR VENCEU!')
    print('\033[30m-' * 30)


