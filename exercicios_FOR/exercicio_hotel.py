def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    return True, cpf


qtde = int(input('Quantas pessoas no quarto? '))

quarto = []

for i in range(qtde):
    nome = input(f'Nome do hóspede {i+1}: ').strip().title()
    
    while True:
        cpf_input = input('CPF: ').strip()
        if validar_cpf(cpf_input)[0]:
            cpf = validar_cpf(cpf_input)[1]
            break
        print('CPF inválido! Tente novamente.')
    
    quarto.append({'nome': nome, 'cpf': cpf})

# Saída
for h in quarto:
    print(f"{h['nome']} - {h['cpf'][:3]}.{h['cpf'][3:6]}.{h['cpf'][6:9]}-{h['cpf'][9:]}")