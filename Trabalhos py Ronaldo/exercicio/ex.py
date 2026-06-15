produto = input("Produto: ")
categoria = input("Categoria (alimento/bebida/limpeza): ")
quantidade = int(input("Quantidade em estoque: "))

if not produto or not categoria or not quantidade:
    print("Digite os campos corretamente")
else:
    if categoria == "alimento".lower():
        estoque = 50

    elif categoria == "bebida".lower():
        estoque = 75

    elif categoria == "limpeza".lower():
        estoque = 30 

    else:
        print("Categoria inválida")
        estoque = 0

    if quantidade < estoque:
        print(f"Solicitar {produto} à equipe de compras. Temos apenas {quantidade} unidades.")
    else:
        print(f"Estoque de {produto} está ok.")