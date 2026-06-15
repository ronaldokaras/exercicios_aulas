populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a < populacao_b:
    populacao_a = round(populacao_a * 1.03) 
    populacao_b = round(populacao_b * 1.015)
    anos += 1

print(f'Serão necessários {anos} anos.')
print(f'População A: {populacao_a:,} habitantes')
print(f'População B: {populacao_b:,} habitantes')