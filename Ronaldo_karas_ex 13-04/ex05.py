print("="* 50)
n1 = float(input("DIGITE SUA PRIMEIRO NOTA: "))
n2 = float(input("DIGITE SUA SEGUNDO NOTA: "))

media = (n1+n2)/2

if media == 10:
    print("aprovado com distinção")
elif media >= 7:
    print("aprovado")
else:
    print("reprovado")