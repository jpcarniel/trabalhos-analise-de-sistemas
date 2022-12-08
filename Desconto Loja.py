ru_4059818 = 'João Paulo Carniel Fonseca'
print('Bem vindo à loja do {}!'.format(ru_4059818))
valor = float(input('Qual valor do produto? '))  # entra com o valor do produto
qnt = int(input('Entre com a quantidade do produto? '))  # entra com a quantidade
sub_total = valor * qnt  # calculamos e armazenamos o valor final, sem desconto
desc = ''  # recebe a porcentagem do desconto
total = ''  # recebe o valor com desconto
if qnt < 9:  # condicional para quantidade menor que 9 unidades
    print('O valor total, sem desconto, é R${:.2f}.'.format(sub_total))  # o programa retorna com o valor sem desconto
    print('Quantidade insuficiente para aplicar desconto.')  # o programa retorna informando que não há desconto
elif 9 < qnt < 100:  # condicional para quantidade entre 10 e 99 unidades
    desc = 5/100  # porcentagem do desconto (5/100 = 5%)
    total = sub_total * (1 - desc)  #  aplicamos o desconto no sub total
    print('O valor total, sem desconto, é R${:.2f}.'.format(sub_total))
    print('O valor total, com desconto, é R${:.2f}. (Desconto de {:.0f}%)'.format(total, desc * 100))
elif 99 < qnt < 1000:  # condicional para quantidade entre 100 e 999 unidades
    desc = 10 / 100  #  desconto de 10%
    total = sub_total * (1 - desc)  # aplicamos o desconto no sub total
    print('O valor total, sem desconto, é R${:.2f}.'.format(sub_total))
    print('O valor total, com desconto, é R${:.2f}. (Desconto de {:.0f}%)'.format(total, desc * 100))
elif qnt > 999:  # condicional para 1000 unidades ou mais
    desc = 15 / 100  # desconto de 15%
    total = sub_total * (1 - desc)  # aplicamos o desconto no sub total
    print('O valor total, sem desconto, é R${:.2f}.'.format(sub_total))
    print('O valor total, com desconto, é R${:.2f}. (Desconto de {:.0f}%)'.format(total, desc * 100))