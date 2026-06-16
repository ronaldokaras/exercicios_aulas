precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

precos_reajustados = {}

for produto, preco in precos.items():
    if preco <= 1000:
        novo_preco = preco * 1.10
    elif preco <= 2000:   
        novo_preco = preco * 1.15
    else:                 
        novo_preco = preco * 1.20
    
    novo_preco = round(novo_preco, 2)
    precos_reajustados[produto] = novo_preco

print("\nPreços atualizados:")
for produto, novo_preco in precos_reajustados.items():
    print(f"{produto}: R$ {novo_preco}")

#===== OU ======

for produto in precos:
    preco_produto = preco[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.10
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.12
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")