produtos = ['tv', 'celular', 'teclado', 'tablet', 'forno', 'geladeira']

estoque = [1000,1500,350,2700,900,70,90,80]

novos_produtos = ['iphome 12', 'oculos']

produtos.extend(novos_produtos)

print(produtos)

#============================================================================

produtos = ['tv', 'celular', 'teclado', 'tablet', 'forno', 'geladeira']

estoque = [1000,1500,350,2700,900,70,90,80]

novos_produtos = ['iphome 12', 'oculos']

todos_produtos = produtos + novos_produtos

print(todos_produtos)

#==================================================
#list.sort()
produtos = ['tv', 'celular', 'teclado', 'tablet', 'forno', 'geladeira']

produtos.sort()

print(produtos)