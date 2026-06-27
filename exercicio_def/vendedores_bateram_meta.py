def bateram_meta(meta,vendas):
    nomes = [nome for nome, valor in vendas.items() if valor>=meta]
    percentual = (len(nomes)/len(vendas)) * 100 
    return (nomes, percentual)

meta = 10000
vendas = {
'João': 15000,
'Julia': 27000,
'Marcus': 9900,
'Maria': 3750,
'Ana': 10300,
'Alon': 7870,
}

lista, perc = bateram_meta(meta,vendas)

print(f"Bateram a meta: {lista}")
print(f'Percentual batido: {perc:.1f}')