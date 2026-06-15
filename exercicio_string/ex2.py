cpf = input("Digite seu CPF ")

# replance pontos, traço e espaço
cpf_limpo = cpf.replace('.','').replace('-', '').replace(' ', '')

if cpf_limpo.isnumeric() and len(cpf_limpo) ==11:
    print(f"Seu Valido {cpf_limpo}")
else:
    print("CPF invalido")