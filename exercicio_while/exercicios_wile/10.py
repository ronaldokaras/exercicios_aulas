salario = 1000.00          
ano = 1995
taxa = 0.015              

print(f"Ano {ano}: R$ {salario:.2f} (inicial)")

ano = 1996
salario = salario * (1 + taxa)   
print(f"Ano {ano}: R$ {salario:.2f} (+{taxa*100:.1f}%)")

for ano in range(1997, 2004):     
    taxa = taxa * 2               
    salario = salario * (1 + taxa)
    print(f"Ano {ano}: R$ {salario:.2f} (+{taxa*100:.1f}%)")