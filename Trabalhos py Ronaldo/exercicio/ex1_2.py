fun1 = float(input("Digite a qntd vend do fun1: "))
fun2 = float(input("Digite a qntd vend do fun2: "))
fun3 = float(input("Digite a qntd vend do fun3: "))

if fun1 >= 2000:
    bonus = fun1 * 1.15
    print(f"\nO valor total com bonus é {bonus:.2f}")
elif fun1 < 2000 or 1000:
    bonus = fun1 * 1.10
    print(f"\nO valor total com bonus é {bonus:.2f}")
else:
    print("\nNão atingiu as metas")

if fun2 >= 2000:
    bonus = fun1 * 1.15
    print(f"\nO valor total com bonus é {bonus:.2f}")
elif fun2 < 2000 or 1000:
    bonus = fun2 * 1.10
    print(f"\nO valor total com bonus é {bonus:.2f}")
else:
    print("\nNão atingiu as metas")

if fun3 >= 2000:
    bonus = fun3 * 1.15
    print(f"\nO valor total com bonus é {bonus:.2f}")
elif fun3 < 2000 or 1000:
    bonus = fun3 * 1.10
    print(f"\nO valor total com bonus é {bonus:.2f}")
else:
    print("\nNão atingiu as metas")
