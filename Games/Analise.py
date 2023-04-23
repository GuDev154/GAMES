soma = 0
maisv = 0
mulher = 0
nomev=""
media=0
print('-----------ANALISADOR----------')
for c in range(1, 3):
    nome = str(input('Nome da {}° pessoa:'.format(c))).strip()
    idade = int(input('Idade da {}° pessoa:'.format(c)))
    sexo = str(input('Sexo da {}° pessoa:(M/F)'.format(c))).upper().strip()
    print('-' * 30)
    soma += idade
    media = soma / 4
    if sexo == 'M':
        if idade > maisv:
            maisv = idade
            nomev = nome
    if sexo =='F':
        if idade<=20:
            mulher+=1
print('A media do grupo é {}'.format(media))
print('O homem mais velho é {} e tem {} anos'.format(nomev,maisv))
print('O numero de mulheres menores de 20 é {}'.format(mulher))
