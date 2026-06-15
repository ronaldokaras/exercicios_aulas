venda = float(input("Valor da Compra: "))

if venda <= 100:
    desconto = 0
    print("Sem descontos")

elif venda < 500:
    desconto = 0.10
    print("Desconto de 10%")

else:     
    desconto = 0.15
    print("Desconto de 15%")

valor_final = venda - (venda * desconto)

print(f"Valor final de R$ {valor_final:.2f}")