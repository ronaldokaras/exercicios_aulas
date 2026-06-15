produto = input('Digite seu produto: ')
produtos = ['tv', 'celular', 'teclado', 'tablet', 'forno', 'geladeira']
qnts = [1000, 1500, 350, 2700, 900, 70]  

if produto not in produtos:
    print("Seu produto não tem no estoque")

else:
    i = produtos.index(produto)  # Pega a posição do produto digitado
    print(f"Seu produto {produto} tem no estoque essa quantidade: {qnts[i]}")