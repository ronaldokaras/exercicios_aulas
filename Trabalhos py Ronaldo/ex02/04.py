consumo = float(input("Digite o Consumo de energia em kWh "))

if consumo <= 100:
    preco = 0.50
    print("Valor da faixa R$ 0,50")
elif consumo <200:
    preco = 0.70
    print("Valor da faixa R$ 0,70")
else:
    preco =  0.90
    print("Valor da faixa R$ 0,90")

total = consumo * preco

print(f"Valor final de R$ ", total)