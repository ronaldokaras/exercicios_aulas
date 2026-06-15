por_hr = float(input("Quanto o Sr. ganha por hora? "))
n_hr = float(input("Quantas horas o Sr. trabalha por mês? "))

bruto = por_hr * n_hr

print("\n" + "="*50)
print("          FOLHA DE PAGAMENTO")
print("="*50)


if bruto <= 900:
    ir = 0
    aliquota_ir = "Isento"
elif bruto <= 1500:
    ir = bruto * 0.05
    aliquota_ir = "5%"
elif bruto <= 2500:
    ir = bruto * 0.10
    aliquota_ir = "10%"
else:
    ir = bruto * 0.20
    aliquota_ir = "20%"


inss = bruto * 0.10
fgts = bruto * 0.11  

descontos = ir + inss
liquido = bruto - descontos


print(f"Salário Bruto                  : R$ {bruto:.2f}")
print(f"(-) IR ({aliquota_ir})          : R$ {ir:.2f}")
print(f"(-) INSS (10%)                 : R$ {inss:.2f}")
print(f"FGTS (11%)                     : R$ {fgts:.2f}")
print("-" * 50)
print(f"Total de descontos             : R$ {descontos:.2f}")
print(f"Salário Líquido                : R$ {liquido:.2f}")
print("="*50)