ru_4059818 = 'João Paulo Carniel Fonseca'
peca = {} #dicionário para os dados das peças
pecas = [] #lista onde iremos guardar os dicionários com os dados de cada peça
cont = 1 #contador para darmos o código de cada peça que formos cadastrando

def cadastrarPeca():
    global cont #para utilizarmos e atualizarmos o valor global da variável cont
    print('-' * 10, 'Cadastrando peça', '-' * 10)
    peca['codigo'] = cont #o codigo de cada peça varia de acordo com o contador
    print('Código da peça: {}'.format(cont))
    peca['nome'] = input('Digite o NOME da peça: ')
    peca['fabricante'] = input('Digite o FABRICANTE da peça: ')
    peca['valor'] = float(input('Digite o VALOR da peça: '))
    pecas.append(peca.copy()) #enviamos o dicionário para dentro da lista
    cont += 1 #atualizando o contador para o próximo cadastro

def consultarPeca():
    while True: #criamos um loop
       print('-' * 10, 'Menu de consulta', '-' * 10)
       print('1 - Consultar todas as peças.')
       print('2 - Consultar por código.')
       print('3 - Consultar por fabricante.')
       print('4 - Retornar.')
       opcao = int(input('Escolha a opção desejada: '))
       if opcao == 1:
           print('-' * 5, 'Mostrando todas as peças', '-' * 5)
           for e in pecas: #para andarmos pelos dicionários na lista de peças
                print('-' * 20)
                for i, j in e.items(): #para andarmos por dentro de cada dicionário
                    print('{}: {}'.format(i, j)) #fazemos o print das chaves e dados de cada dicionário
       elif opcao == 2:
            cod_busca = int(input('Digite o código: '))
            for e in pecas: #para andarmos pelos dicionarios na lista de peças
                if cod_busca == e['codigo']: #verificamos se o código inserido é igual ao dado da chave 'codigo'
                    print('-' * 5, 'Peça filtrada por código', '-' * 5)
                    for i, j in e.items(): #para andarmos dentro do dicionário com o código certo
                        print('{}: {}'.format(i, j)) #fazemos o print das chaves e dados do dicionário escolhido
       elif opcao == 3:
           nome_busca = input('Digite o fabricante: ')
           for e in pecas: #para andarmos pelos dicionarios na lista de peças
                if nome_busca == e['fabricante']: #verificamos se o nome do fabricante inserido é igual ao dado da chave 'fabricante'
                    print('-' * 5, 'Peças filtradas por fabricante', '-' * 5)
                    for i, j in e.items(): #para andarmos dentro dos dicionários com o fabricante digitado
                        print('{}: {}'.format(i, j)) #fazemos o print das chaves e dados do dicionário escolhido
       elif opcao == 4:
           break #quebramos o loop e voltamos para o menu anterior

def removerPeca():
    cod = int(input('Digite o código da peça que deseja remover do cadastro: '))
    for e in pecas: #para andarmos pelos dicionarios na lista de peças
        if cod == e['codigo']: #verificamos se o código inserido é igual ao dado da chave 'codigo' de algum dicionario
            pecas.remove(e)  #se o código bater, removemos o dicionário do mesmo de dentro da lista de peças
            print('Peça removida com sucesso.')

#programa principal
print('Bem vindo ao Controle De estoque da Bicicletaria do {}!'.format(ru_4059818))
while True: #criamos um loop
    try: #para evitar erros de ValueError e o programa encerrar precocemente
        print('-' * 10, 'Menu inicial', '-' * 10)
        print('1 - Cadastrar peças.')
        print('2 - Consultar peças.')
        print('3 - Remover peças.')
        print('4 - Sair.')
        res = int(input('Escolha uma opção: '))
        if res == 1:
            cadastrarPeca()
        elif res == 2:
            consultarPeca()
        elif res == 3:
            removerPeca()
        elif res == 4:
            print('Encerrando programa...')
            break #quebramos o loop para encerrar o programa
            #
        else:
            print('Opção inválida.')
    except ValueError:\
        print('Insira uma opção válida.')
