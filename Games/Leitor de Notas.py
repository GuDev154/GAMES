dados=[]
media=0
while True:
    nome=str(input('Nome:')).strip()
    n1=float(input('Nota 1°:'))
    n2=float(input('Nota 2°:'))
    media=(n1+n2)/2
    dados.append([nome,[n1,n2],media])
    r=str(input('Deseja continuar?(S/N)')).strip().upper()
    if r=='N':
        break
print('-'*30)
print(f'{"No":>4} {"Nome":<10} {"Média":>8}')
for i,a in enumerate(dados):
    print(f'{i:>4} {a[0]:<10} {a[2]:>8}')
print('-'*30)
print('Digite 999 Para Finalizar...')
while True:
    opc=int(input('Digite a numeração do aluno para ver suas notas:'))
    if opc<=len(dados)-1:
        print(f'As notas do {dados[opc][0]} são {dados[opc][1]}')
    if opc==999:
       break
print('Programa Finalizado!')