qtde_pessoa = int(input('Qauntas pessoas terão no quarto? '))

if qtde_pessoa >4:
    print('quarto lotado ou não ha vagas disponiveis')
else:
    quarto = []
    for i in range(qtde_pessoa):
        nome = input('Qual o nome? ')
        cpf = input('Qual o cpf? ')
        
        if len(cpf) <11:
            print('Digite o CPF correto')
        else:
            hospede = [nome, f'cpf: {cpf}']
            quarto.append(hospede)

print(quarto)