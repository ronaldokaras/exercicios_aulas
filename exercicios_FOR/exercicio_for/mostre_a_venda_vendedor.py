vendas = [1000, 1500, 2000, 2500, 3000]
vendedores = ["João", "Maria", "Pedro", "Ana", "Carlos"]
for i in range(len(vendas)):
    print(f"Vendedor: {vendedores[i]}, Venda: R${vendas[i]:.2f}")