fun1 = float(input("Digite a qntd vend do fun1: "))
fun2 = float(input("Digite a qntd vend do fun2: "))
fun3 = float(input("Digite a qntd vend do fun3: "))

meta = 1000

if fun1 >= meta:
    bonus = fun1 * 1.10
    print(f"O valor total com bonus é {bonus:.2f}")
else:
    print("metas não atendidas, sem bonus")

if fun2 >= meta:
    bonus = fun2 * 1.10
    print(f"O valor total com bonus é {bonus:.2f}")
else:
    print("metas não atendidas, sem bonus")

if fun3 >= meta:
    bonus = fun3 * 1.10
    print(f"O valor total com bonus é {bonus:.2f}")
else:
    print("metas não atendidas, sem bonus")
