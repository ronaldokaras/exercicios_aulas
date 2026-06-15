n1 = float(input("DIGITE SEU PRIMEIRO NUMERO: "))
n2 = float(input("DIGITE SEU SEGUNDO NUMERO: "))
n3 = float(input("DIGITE SEU TERCEIRO NUMERO: "))

numeros = sorted([n1, n2, n3], reverse=True)

print("\n=== ORDEM DECRESCENTE ===")
print(f"1º lugar (maior):  {numeros[0]}")
print(f"2º lugar:          {numeros[1]}")
print(f"3º lugar (menor):  {numeros[2]}")