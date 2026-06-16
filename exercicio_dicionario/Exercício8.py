vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

vendas_23_ajustado = {}

for mes, valor_22 in vendas_22.items():
    valor_23 = vendas_23[mes]
    if valor_23 < valor_22:
        vendas_23_ajustado[mes] = valor_22  
    else:
        vendas_23_ajustado[mes] = valor_23

total_22 = sum(vendas_22.values())
total_23_ajustado = sum(vendas_23_ajustado.values())

crescimento = (total_23_ajustado - total_22) / total_22 * 100

print("Vendas 2022 (original):", vendas_22)
print("Vendas 2023 ajustadas :", vendas_23_ajustado)
print(f"Total 2022: R$ {total_22}")
print(f"Total 2023 ajustado: R$ {total_23_ajustado}")
print(f"Crescimento ajustado: {crescimento:.2f}%")

#==== Outras formas =====

# Usando .items() – mais legível quando precisamos da chave e do valor juntos
for mes, valor_22 in vendas_22.items():
    ...

# Usando .keys() – equivalente, mas mais verboso
for mes in vendas_22.keys():
    valor_22 = vendas_22[mes]
    ...

# .values() – quando só interessam os valores (ex: soma, média)
soma = sum(vendas_22.values())