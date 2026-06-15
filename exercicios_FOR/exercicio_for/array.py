vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]

faixas = [0, 0, 0, 0, 0, 0, 0, 0, 0]  

for venda in vendas:
    salario = 200 + (0.09 * venda)
    
    if salario >= 200 and salario <= 299:
        faixas[0] += 1
    elif salario >= 300 and salario <= 399:
        faixas[1] += 1
    elif salario >= 400 and salario <= 499:
        faixas[2] += 1
    elif salario >= 500 and salario <= 599:
        faixas[3] += 1
    elif salario >= 600 and salario <= 699:
        faixas[4] += 1
    elif salario >= 700 and salario <= 799:
        faixas[5] += 1
    elif salario >= 800 and salario <= 899:
        faixas[6] += 1
    elif salario >= 900 and salario <= 999:
        faixas[7] += 1
    else:
        faixas[8] += 1

print(f"$200 - $299  : {faixas[0]} vendedor(es)")
print(f"$300 - $399  : {faixas[1]} vendedor(es)")
print(f"$400 - $499  : {faixas[2]} vendedor(es)")
print(f"$500 - $599  : {faixas[3]} vendedor(es)")
print(f"$600 - $699  : {faixas[4]} vendedor(es)")
print(f"$700 - $799  : {faixas[5]} vendedor(es)")
print(f"$800 - $899  : {faixas[6]} vendedor(es)")
print(f"$900 - $999  : {faixas[7]} vendedor(es)")
print(f"$1000 em diante: {faixas[8]} vendedor(es)")


#===================================

vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]

faixas = [0, 0, 0, 0, 0, 0, 0, 0, 0]
limites_faixas = [299, 399, 499, 599, 699, 799, 899, 999, float('inf')]

for venda in vendas:
    salario = 200 + (0.09 * venda)
    
    indice = 0
    while salario > limites_faixas[indice]:
        indice += 1
    
    faixas[indice] += 1
    print(f"Venda: ${venda:,.0f} → Salário: ${salario:.2f} → Faixa {indice+1}")

nomes_faixas = [
    "$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
    "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999",
    "$1000 em diante"
]

for i in range(len(faixas)):
    print(f"{nomes_faixas[i]:<15} : {faixas[i]} vendedor(es)")