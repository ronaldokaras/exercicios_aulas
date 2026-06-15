#fruta = input("Digite o nome de uma fruta: ")

#frutas = []

#while fruta !='':
 #   frutas.append(fruta)
  #  fruta = input('Digite o nome de uma fruta: ')
#print('Frutas registradas: ')
#for f in frutas:
 #   print(f)


#=================

vendas = []
while True:
    produto = input('Registre um produto. Para encerrar o programa, aperte enter com a caixa vazia: ')
    if not produto:
        break
    qtde = int(input('Digite a quantidade vendida: '))
    vendas.append((produto, qtde))
print('Produtos registrados: ')
for produto, qtde in vendas:
    print(f'{produto}: {qtde} unidades vendidas')







    