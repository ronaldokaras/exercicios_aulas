precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

print("Preços dos Itens antes do ajuste:")
for produto, preco in precos.items():
    print(f"{produto}: R$ {preco}")

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

print("\nDetalhamento dos reajustes:")
for produto, preco_antigo in precos.items():
    novo = precos_reajustados[produto]
    if preco_antigo <= 1000:
        percentual = "10%"
    elif preco_antigo <= 2000:
        percentual = "15%"
    else:
        percentual = "20%"
    print(f"{produto}: R$ {preco_antigo} → R$ {novo} (+{percentual})")