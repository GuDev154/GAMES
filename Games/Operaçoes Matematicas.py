import random


def titulo(msg):
   print('-'*40)
   print(f'{msg:^10}')
   print('-'*40)


titulo('    EFETUANDO OPERAÇOES MATEMATICAS')
print('Para Finalizar o Programa digite 00!')
print('-' * 40)
correto=0

while True:
   n1=random.randint(1,20)
   n2=random.randint(1,20)
   soma=n1+n2
   subtracao=n1-n2
   r1=int(input(f'{n1} + {n2} = '))
   r2=int(input(f'{n1} - {n2} = '))
   print('-' * 40)
   if r1==soma and r2==subtracao:
      print('Resultado correto!')
      print('-' * 40)
      correto+=1
   elif r1==00 or r2==0:
      break
   else:
      print(f'Resultado incorreto!')
      print(f'Soma = {soma} e Subtração = {subtracao}')
      print('-' * 40)
print('PROGRAMA FINALIZADO!')
print(f'O total de respostas corretas foi {titulo(correto)}!')