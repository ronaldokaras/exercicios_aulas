vendas = ('Lira', '25/06/2024', 1500.00, 'Estagiaria')

nome =vendas[0]
data_contratacao = vendas[1]
salario = vendas[2]
cargo = vendas[3]

print(f"Nome: {nome} - Data da contratação: {data_contratacao} - Salário: {salario} - Cargo: {cargo}")

#== Desempacotamento de tupla ==#
nome, data_contratacao, salario, cargo = vendas