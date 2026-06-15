cpf = input("Digite seu CPF ")

if cpf.isnumeric() and len(cpf) ==11:
    print("Seu Valido")
else:
    print("CPF invalido")