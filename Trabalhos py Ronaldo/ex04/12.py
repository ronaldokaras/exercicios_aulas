por_hr = float(input("Quanto o Sr. ganha por hora? "))
n_hr = float(input("Quantas hora o Sr. trabalha por mês? "))

bruto = por_hr*n_hr
desc_ir = bruto * 0.11
desc_inss = bruto * 0.08
desc_sind = bruto * 0.05

desc_total = desc_inss + desc_ir + desc_sind
liqui = bruto - desc_total

print(f"Bruto: {bruto:.2f}")
print(f"IR (11%): {desc_ir:.2f}")
print(f"INSS (8%): {desc_inss:.2f}")
print(f"Sindicato (5%): {desc_sind:.2f}")
print(f"Total de descontos: {desc_total:.2f}")
print(f"liquido: {liqui:.2f}")