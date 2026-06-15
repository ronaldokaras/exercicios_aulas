def calcular_bonus_progressivo(venda):
    if venda <= 10000:
        return venda * 0.05      # 5%
    elif venda <= 20000:
        return venda * 0.08      # 8%
    elif venda <= 30000:
        return venda * 0.10      # 10%
    else:
        return venda * 0.15      # 15%


# ==================== Programa com Input ====================

print("=== CÁLCULO DE BÔNUS PROGRESSIVO ===\n")
print("Digite os dados dos vendedores (0 para encerrar)\n")

vendedores = []
total_vendas = 0
total_bonus = 0

while True:
    nome = input("Nome do vendedor (ou 0 para encerrar): ").strip()
    if nome == '0' or nome.lower() == 'sair':
        break
    
    try:
        venda = float(input(f"Vendas de {nome}: R$ "))
    except ValueError:
        print("Valor inválido! Tente novamente.\n")
        continue
    
    bonus = calcular_bonus_progressivo(venda)
    
    vendedores.append((nome, venda, bonus))
    total_vendas += venda
    total_bonus += bonus
    
    print(f"Bônus calculado: R$ {bonus:,.2f}\n")


# ==================== Relatório Final ====================
if vendedores:
    print("\n" + "="*60)
    print("RELATÓRIO DE BÔNUS PROGRESSIVO")
    print("="*60)
    
    for nome, venda, bonus in vendedores:
        print(f"{nome:12} | Vendas: R$ {venda:10,.2f} | Bônus: R$ {bonus:9,.2f}")
    
    print("-" * 60)
    print(f"Total de Vendedores : {len(vendedores)}")
    print(f"Total de Vendas     : R$ {total_vendas:,.2f}")
    print(f"Total de Bônus      : R$ {total_bonus:,.2f}")
else:
    print("Nenhum vendedor cadastrado.")