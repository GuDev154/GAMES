import random
c=random.randint(1,10)
r=0
contr=0
print('----------\033[30mJOGO DA ADIVINHAÇÃO\033[m-----------')
print('Advinhe um número de 1 - 10')
print('-'*40)
while r!= c:
    r=int(input('Qual seu palpite? '))
    print('-'*40)
    if r!=c:
      print('\033[31mTente Novamente!\033[m')
      contr+=1
    if r>c:
      print('Menos...Menos...')
      print('-' * 40)
    if r<c:
      print('Mais...Mais...')
      print('-' * 40)
print('\033[32mPARABÉNS você ACERTOU com {} tentativas!\033[m'.format(contr+1))
print('-'*40)