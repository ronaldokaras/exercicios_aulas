precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

pesquisar = input("Digite o nome de um produto: ")

for produto, valor in precos.items():
    if produto in pesquisar:
        print(f"{produto} no valor de {valor}")
else:
    print('Produto não cadastrado')
    