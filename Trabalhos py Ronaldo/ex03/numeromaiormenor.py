numero = float(input("Digite um numero: "))
numero1 = float(input("Digite um numero: "))

if numero > numero1:
    print(f"Primeiro Numero Maior {numero:.0f}")
elif numero1 > numero:
    print(f"Segundo Numero Maior {numero1:.0f}")
else:
    print("numeros iguais")