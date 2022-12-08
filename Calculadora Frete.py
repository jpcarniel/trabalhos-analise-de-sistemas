ru_4059818 = 'João Paulo Carniel Fonseca' #identificador pessoal
print('Bem vindo à Companhia de Logística de {}.'.format(ru_4059818))
def dimensoesObjeto(): #função para definirmos o tamanho do objeto
    while True: #abrimos um loop para retornamos ao início do programa caso algum input seja inválido
        try: #para tratarmos erros na hora de inserir as dimensões sem que o programa encerre
            alt = int(input('Insira a altura do volume (em cm): '))
            comp = int(input('Insira o comprimento do volume (em cm): '))
            larg = int(input('Insira a largura do volume (em cm): '))
            volume = alt * comp * larg #calculamos o volume com os inputs fornecidos
            print('O volume do produto é {}cm³.'.format(volume))
            if volume <= 1000:
                return 10 #retornamos o valor de acordo com o volume
            elif 1000 < volume <= 10000:
                return 20
            elif 10000 < volume <= 30000:
                return 30
            elif 30000 < volume <= 100000:
                return 50
            elif volume > 100000:
                print('Não aceitamos volumes com dimensões tão grandes.') #para informar que o volume não é aceito
                continue #para voltar ao começo do loop e poder inserir valores válidos
        except ValueError: #para tratar um possível erro na hora de inserir as dimensões
                print('Insira uma dimensão válida.')

def pesoObjeto(): #função para definirmos o multiplicador do preço de acordo com o peso
    while True: #abrimos um loop para retornamos ao início do programa caso o input seja inválido
        try: #para tratarmos erros na hora de inserir o peso sem que o programa encerre
            peso = float(input('Digite o peso do produto em kg: '))
            if peso < 0.1:
                return 1 #retornamos o multiplicador de acordo com o peso
            elif 0.1 < peso <= 1:
                return 1.5
            elif 1 < peso <= 10:
                return 2
            elif 10 < peso <= 30:
                return 3
            elif peso > 30:
                print('Não aceitamos produtos tão pesados.') #para informar que o peso não é aceito
                continue #para voltar ao começo do loop e poder inserir um peso válido
        except ValueError: #para tratar um possível erro na hora de inserir o peso
                print('Insira um peso válido.')

def rotaObjeto(): #função para descobrirmos o multiplicador de acordo com a rota desejada
    while True: #abrimos um loop para retornamos ao início do programa caso o input seja diferente dos oferecidos
        print('Rotas disponíveis: ')
        print('PB - Porto Alegre > Bagé')
        print('PR - Porto Alegre > Rio Grande')
        print('BP - Bagé > Porto Alegre')
        print('BR - Bagé > Rio Grande')
        print('RB - Rio Grande > Bagé')
        print('RP - Rio Grande > Porto Alegre')
        rota = input('Digite a rota desejada: ')
        if rota in 'pb PB bp BP': #para não diferenciar maiusculo e minusculo
            return 1 #retornamos o multiplicador de acordo com a rota
        elif rota in 'pr PR rp RP':
            return 1.2
        elif rota in 'rb RB br BR':
            return 1.5
        else:
            print('Rota inexistente, tente novamente.') #aviso caso a rota seja inválida
            continue #no caso da rota ser inválida, retorna ao começo do loop

#programa principal
valor = dimensoesObjeto()
multiplicador_peso = pesoObjeto()
multiplicador_rota = rotaObjeto()
valor_total = valor * multiplicador_peso * multiplicador_rota
print('Valor total do frete: R${:.2f}. (volume: {} * peso: {} * rota: {})'.format(valor_total, valor, multiplicador_peso, multiplicador_rota))
input('Aperte ENTER para sair.')
print('Encerrando o programa...')
