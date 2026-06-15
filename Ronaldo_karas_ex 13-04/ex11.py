sala = float(input("Quanto o Sr. ganha por mês? "))

print("-" * 50)

if sala <= 280:
    percentual = 20
    aumento = sala * 1.20
elif sala <= 700:
    percentual = 15
    aumento = sala * 1.15
elif sala <= 1500:
    percentual = 10
    aumento = sala * 1.10
elif sala > 1500:
    percentual = 5
    aumento = sala * 1.05
else:
    print("Valor inválido!")
    exit()

valor_aumento = aumento - sala
novo_salario = aumento

print(f"Salário antes do reajuste     : R$ {sala:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento              : R$ {valor_aumento:.2f}")
print(f"Salário após o reajuste       : R$ {novo_salario:.2f}")

print("-" * 50)