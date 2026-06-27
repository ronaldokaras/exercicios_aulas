
cardapio = {
    1: ("Cachorro-Quente", 5.50),
    2: ("Bauru Simples", 1.00),
    3: ("Bauru com ovo", 2.00),
    4: ("Hambúrguer", 3.50),
    5: ("Cheeseburguer", 2.50),
    6: ("Refrigerante", 2.00)
    }   

total_geral = 0.0

print("=" * 40)
print("CARDÁPIO")
print("Código - Item - Preço")
for cod, (nome, preco) in cardapio.items():
    print(f"{cod} - {nome} - R$ {preco:.2f}")
print("Para encerrar o pedido, digite 0 no código.")
print("=" * 40)

while True:
    try:
        codigo = int(input("\nDigite o código do produto: "))
        if codigo == 0:
            break
        
        if codigo not in cardapio:
            print("Código inválido! Tente novamente.")
            continue
        
        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero. Tente novamente.")
            continue
        
        nome, preco = cardapio[codigo]
        subtotal = preco * quantidade
        total_geral += subtotal
        
        print(f"Item: {nome} | Quantidade: {quantidade} | Subtotal: R$ {subtotal:.2f}")
    
    except ValueError:
        print("Entrada inválida! Digite números inteiros para código e quantidade.")

print("\n" + "=" * 40)
print(f"TOTAL GERAL DO PEDIDO: R$ {total_geral:.2f}")
print("=" * 40)