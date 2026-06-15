venda = input('registre um produto. Para encerrar o programa, aperte enter com a caixa vazia: ')

vendas = []

while venda != '':
    vendas.append(venda)

    venda = input('Registre um produto. Para cancelar o registro, aperte enter com a caixa vazia: ')

print('Produtos registrados: ')
