print('exercício 1 - Analise de vendas - Desempacotamento de tupla')

meta= 10000

vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870)
]

for item in vendas:
    nome, vendas = item
    if vendas >= meta:
        print(f'{nome} alcançou a meta')