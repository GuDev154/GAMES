c=('\033[44;30m', #Azul
   '\033[m')     #Sem cor


def ajuda(com=''):
        help(com)


def titulo(msg,cor=0):
    ajuste=len(msg)+10
    print(c[cor])
    print('-'*ajuste)
    print(f'     {msg}')
    print('-'*ajuste)
    print(c[cor])


while True:
    titulo('SISTEMA DE AJUDA PYHELP',)
    comend=str(input('Bibliotecas ou Funções->'))
    if comend.upper()=='FIM':
        print('Encerrando..')
        break
    else:
        ajuda(comend)
titulo('ATÉ LOGO!',)