ru_4059818 = 'João Paulo Carniel Fonseca'  # identificador pessoal
print('Bem vindo à lanchonete do {}!'.format(ru_4059818))
print('*' * 16, 'Cardápio', '*' * 16)
print('| Código |', '      Descrição      ', '| Valor |')
print('|   100  |', '   Cachorro Quente   ', '|  9,00 |')
print('|   101  |', 'Cachorro Quente Duplo', '| 11,00 |')
print('|   102  |', '        X-Egg        ', '| 12,00 |')
print('|   103  |', '      X-Salada       ', '| 12,00 |')
print('|   104  |', '       X-Bacon       ', '| 14,00 |')
print('|   105  |', '       X-Tudo        ', '| 17,00 |')
print('|   200  |', '  Refrigerante Lata  ', '|  5.00 |')
print('|   201  |', '     Chá Gelado      ', '|  4,00 |')
total = 0  #  onde vamos armazenar a soma dos valores dos pedidos
while True:  # abrimos o loop do programa até invocarmos o break quando o cliente não quiser pedir mais
    codigo = int(input('Digite o código do produto desejado: '))
    if codigo == 100:
        total = total + 9  #  adicionamos o valor do produto ao valor total
        print('Você pediu um Cachorro Quente no valor de R$9,00.')
    elif codigo == 101:  # utilizamos elif ao invés de if para o programa não precisar checar cada condição subsequente
        total = total + 11
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00.')
    elif codigo == 102:
        total = total + 12
        print('Você pediu um X-Egg no valor de R$12,00.')
    elif codigo == 103:
        total = total + 12
        print('Você pediu um X-Salada no valor de R$12,00.')
    elif codigo == 104:
        total = total + 14
        print('Você pediu um X-Bacon no valor de R$14,00.')
    elif codigo == 105:
        total = total + 17
        print('Você pediu um X-Tudo no valor de R$17,00.')
    elif codigo == 200:
        total = total + 5
        print('Você pediu um Refrigerante Lata no valor de R$5,00.')
    elif codigo == 201:
        total = total + 4
        print('Você pediu um Chá Gelado no valor de R$4,00.')
    else:  #  no caso de nenhuma das condições anteriores forem verdadeiras
        print('Opção inválida.')
        continue  #  para voltar ao começo do loop
    print('Deseja adicionar mais algum item ao seu pedido? ')
    print('1 - Sim')
    print('2 - Não')
    adicionar = int(input('>> '))  #  váriavel onde vamos armazenar o valor para validarmos a quebra do loop
    if adicionar == 2:  #  condicão para quebrar o loop
        break  # para quebrar o loop
print('O valor total a ser pago é R${:.2f}.'.format(total))
input('Aperta qualquer tecla para sair.')
