while True:
    faturamentos = [] 
    
    for i in range(1, 6):
        valor = float(input(f"Faturamento do mês {i}: R$ "))
        faturamentos.append(valor)
        
    total = sum(faturamentos)
    media = total / 5

    print(f"Faturamento Total (5 meses): R$ {total:,.2f}")
    print(f"Faturamento Médio por mês : R$ {media:,.2f}") 

    break