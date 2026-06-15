idades = [35, 32, 50, 33, 48, 50, 33, 48, 22, 49, 35, 38, 20, 47, 49, 48, 34, 21, 48, 44, 48, 30, 25, 42, 42, 23, 25, 23, 38, 35]

salarios = [3739, 2219, 3554, 3978, 4014, 3270, 4792, 3879, 2981, 2384, 4826, 2460, 3680, 4318, 1872, 1770, 4640, 3929, 3295, 1729, 3965, 4267, 4007, 1916, 2987, 2943, 3852, 4543, 2055, 1730]

media_salarios = sum(salarios) / len(salarios)

# Conta funcionários com idade > 25 e salário < média
resultado = sum(1 for i in range(len(idades)) if idades[i] > 25 and salarios[i] < media_salarios)

print(f"Média salarial: R$ {media_salarios:.2f}")
print(f"Funcionários com >25 anos e salário abaixo da média: {resultado}")