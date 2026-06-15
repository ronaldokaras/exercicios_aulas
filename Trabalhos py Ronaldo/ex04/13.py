
area = float(input("Digite a área a ser pintada em m²: "))

tamanho_lata = 54
valor_lata = 80.0

quant_lata = area / tamanho_lata

preco_total = quant_lata * valor_lata

print(f"Quantidade de latas necessárias: {quant_lata:.2f}")
print(f"Preço total: R$ {preco_total:.2f}")