vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai":16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai":16000, "jun": 18500}

crescimentos = {}

for mes in vendas_22.keys():
    v22 = vendas_22[mes]
    v23 = vendas_23[mes]
    crescimento = ((v23 - v22) / v22) * 100
    crescimentos[mes] = crescimento
    print(f"{mes}: {crescimento:.2f}%")

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())

crescimento_total = ((total_23 - total_22) / total_22) * 100
print(f"\nTotal de vendas 2022: R$ {total_22:,.2f}")
print(f"Total de vendas 2023: R$ {total_23:,.2f}")
print(f"Crescimento total de 2023 em relação a 2022: {crescimento_total:.2f}%")

