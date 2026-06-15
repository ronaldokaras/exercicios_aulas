produtos = ['coca','pepsi','guarana','sprit','fanta']
producao = [15000,12000,13000, 5000,250]

for i in range(5):
    print('{} unidades produzidas de {}'.format('100','coca'))

for i in range(5):
    print('{} unidades produzidas de {}'.format(producao[i],produtos[i]))

tamanho = len(produtos) #conta a quantidade de produtos
for i in range(tamanho):
    print('{} unidades produzidas de {}'.format(producao[i],produtos[i]))