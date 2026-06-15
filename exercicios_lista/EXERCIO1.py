meses = ['jan', ' fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'agost', 'set', 'out', 'nov', 'dez']
vendas1 = [1000,1500,350,2700,900,701,9031]
vendas2 = [19850, 20120,17540,15555,8899]

vendas_ano = vendas1 + vendas2

max_vendido = max(vendas_ano)
min_vendido = min(vendas_ano)

index_maior = vendas_ano.index(max_vendido)
index_menor = vendas_ano.index(min_vendido)

melhor_mes = meses[index_maior]
pior_mes =meses[index_menor]

print(f'O melhor vendido {melhor_mes} com R$ {max_vendido}')
print(f'O menor vendido {pior_mes} com R$ {min_vendido}')