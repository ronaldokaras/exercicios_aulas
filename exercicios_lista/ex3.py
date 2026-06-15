produtos = ['tv', 'celular', 'teclado', 'tablet', 'forno', 'geladeira']

estoque = [1000,1500,350,2700,900,70,90,80]

i = produtos.index('geladeira')#posição do produto
qtd_estoque = estoque[i]

print(f"produto: {i} e em estoque: {qtd_estoque}")