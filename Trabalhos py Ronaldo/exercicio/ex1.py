venda = float(input("Digite a quantidade vendida no mes: "))


if venda >= 50.000:
    print(f"BATIMOS A META! vendemos {venda:.0f} unidades")
else:
    print("META NÂO BATIDA...")