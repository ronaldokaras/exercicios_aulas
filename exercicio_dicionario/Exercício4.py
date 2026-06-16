precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

pesquisar = input("Digite o nome de um produto: ").strip().lower()

if pesquisar in precos:
    print(f"{pesquisar} no valor de {precos[pesquisar]}")
else:
    print("Produto não cadastrado.")
    resposta = input("Deseja cadastrar? (S/N): ").strip().upper()
    if resposta == "S":
        novo_valor = float(input(f"Digite o valor para {pesquisar}: "))
        precos[pesquisar] = novo_valor
        print(f"{pesquisar} cadastrado com sucesso no valor de {novo_valor}.")
    else:
        print("Operação cancelada.")