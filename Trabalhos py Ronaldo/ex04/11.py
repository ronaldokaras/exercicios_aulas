h = float(input("Digite sua altura: "))
s = input("Digite seu sexo (M,F): ").strip().lower()

if s == "m":
    p = (72.7 * h) - 58
    print("Seu peso idadeal é :",p)
elif s == "f":
    p = (62.1 * h) - 44.7
    print("Seu peso idadeal é :",p)
else:
    p = None
    print("Sexo inválido")
