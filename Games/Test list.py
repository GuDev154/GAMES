import random
from time import sleep
from operator import itemgetter
rank={}
jogadores={'Jogador1':random.randint(1,6),'Jogador2':random.randint(1,6),
           'Jogador3':random.randint(1,6),'Jogador4':random.randint(1,6)}
print('-'*30)
for k,v in jogadores.items():
    print(f'      {k} tirou {v}!')
    sleep(0.5)
print('-'*30)
rank=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('  == Rank dos Jogadores ==')
for i,v in enumerate(rank):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}!')
print('-'*30)