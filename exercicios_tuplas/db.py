vendas = [
    ('21/08/2021', 'ipad', 'azul', '128gb', 300,2500.00),
    ('15/02/2022', 'notebook', 'preto', '256gb', 350,3500.00),
    ('10/11/2023', 'smartphone', 'vermelho', '64gb', 150,1500.00),
    ('05/05/2024', 'tablet', 'branco', '128gb', 200,2000.00),
    ('30/09/2024', 'smartwatch', 'preto', '32gb', 80,800.00)
]

data, produto, cor, armazenamento, unidade, valor = vendas[0]

faturamento = unidade * valor
print(faturamento)

#--- ou ---

for item in vendas:
    data, produto, cor, armazenamento, unidade, valor = item
    print(produto, unidade, valor)

faturamento = []

for item in vendas:
    data, produto, cor, armazenamento, unidade, valor = item
    if produto == 'notebook' and data == '15/02/2022':
        print(produto)
        faturamento += unidade * valor
print(faturamento)


