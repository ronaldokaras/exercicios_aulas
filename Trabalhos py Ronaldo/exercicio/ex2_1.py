estoque_alimento = 50
estoque_bebida = 75
estoque_limpeza = 30

alimento = int(input("alimento: "))
bebida = int(input("bebida: "))
limpeza = int(input("limpeza: "))

if alimento <= estoque_alimento:
    print("estoque de alimento ok")
else:
    print("comprar alimento")

if bebida <= estoque_bebida:
    print("estoque de bebida ok")
else:
    print("comprar bebida")

if limpeza <= estoque_limpeza:
    print("estoque de limpeza ok")
else:
    print("comprar limpeza")