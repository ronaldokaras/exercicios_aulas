n1 = float(input("Digite sua nota 1 : "))
n2 = float(input("Digite sua nota 2 : "))
n3 = float(input("Digite sua nota 3 : "))
n4 = float(input("Digite sua nota 4 : "))

mediafinal = (n1+n2+n3+n4)/4

if mediafinal >=7.0:
    print(f"A média: {mediafinal:.1f} - aprovado")
else:
    print(f"A media: {mediafinal:.1f} - reprovado")