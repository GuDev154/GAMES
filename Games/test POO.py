tempos=[]

def linha():
    print('--'*15)
def menu():
    print('== GERENCIADOR DE TRIATLON ==')
    print('[1] - Bicicleta')
    print('[2] - Corrida')
    print('[3] - Natação')
    print('[4] - Fechar App')

def operador():
    print('[1] - Tempo')
    print('[2] - Listar Tempo')
    print('[3] - Melhor Tempo')


def funcoes():
    if escolha == 1:
        tempo = float(input('Informe o tempo decorrido:'))
        tempos.append(tempo)
        print('Tempo Cadastrado com sucesso!')
    elif escolha == 2:
        for v in tempos:
            print(f'- {v} Horas de Prova')
    elif escolha == 3:
        print(f'O melhor tempo foi {min(tempos)}')


while True:
    menu()
    linha()
    opcao=int(input('Informe a Modalidade desejada:'))
    linha()
    if opcao==1:
        print('[BICICLETA] - Menu de Operaçoes')
        operador()
        escolha = int(input('Informe a Modalidade desejada:'))
        funcoes()
    elif opcao==2:
        print('[CORRIDA] - Menu de Operaçoes')
        operador()
        escolha = int(input('Informe a Modalidade desejada:'))
        funcoes()
    elif opcao==3:
        print('[NATAÇÃO] - Menu de Operaçoes')
        operador()
        escolha = int(input('Informe a Modalidade desejada:'))
        funcoes()
    elif opcao==4:
        print('[FINALIZANDO]...')
        break
    else:
        print('[ERRO] - Digite novamente!')