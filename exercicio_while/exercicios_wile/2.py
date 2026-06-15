while True:
    nome = input('Digite seu nome: ')
    if len(nome) >= 3:
        break
    print('Nome inválido. Por favor, digite seu nome com pelo menos 3 caracteres.')

while True:
    idade = input('Digite sua idade: ')
    
    if idade.isdigit() and 0 <= int(idade) <= 150:
        break
    
    print('Idade inválida. Por favor, digite uma idade válida.')

while True:
    salario = float(input('Digite seu salário: '))
    if salario.replace('.', '').isdigit() and float(salario) > 0:
        break
    print('Salário inválido. Por favor, digite um salário válido.')

while True:
    sexo = input('Digite seu sexo (M/F): ')
    if sexo.upper() in ['M', 'F']:
        break
    print('Sexo inválido. Por favor, digite M para masculino ou F para feminino.')

while True:
    estado_civil = input('Digite seu estado civil (S/C/V/D): ')
    if estado_civil.upper() in ['S', 'C', 'V', 'D']:
        break
    print('Estado civil inválido. Por favor, digite S para solteiro, C para casado, V para viúvo ou D para divorciado.')

print('Obrigado por participar!')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: {salario}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estado_civil}')