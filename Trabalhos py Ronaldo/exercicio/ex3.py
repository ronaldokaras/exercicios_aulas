venda = float(input("Digite sua quantidade de vendas: "))

meta = 20.000

if venda < 15.000:
    print(f"meta nao batida {venda}")
elif venda >= 15.000:
    meta = 0.03 * venda
    print("Ganhou um bonus de {}".format(meta))
else:
    print("Meta não atendida , sem bonus")