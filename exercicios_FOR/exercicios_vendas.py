meta = 10000

vendas= [
    ['joao',1500],
    ['marcos',2200],
    ['antonio',1222],
    ['lucia',10900],
    ['evenlin',12345],
    ['claudio',124443]
]

for item in vendas:
    if item[1] >= meta:
        print(f'Vendedor {item[0]} bateu a meta. Fez {item[1]} vendas')
    elif item[1] < meta:
        print(f'O vendedor {item[0]} não bateu a meta')
