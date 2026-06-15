vendas = [1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100,999,900,880,870,1111,120,300,450,800]
meta= 1000

qtde = 0
   
for venda in vendas:
    if venda >= meta:
     qtde += 1
print('{} pessoas bateram a meta'.format(qtde))

#===============================================================
# % batido

vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 
          90, 80, 1100, 999, 900, 880, 870, 1111, 120, 300, 450, 800]
meta = 1000

qtde = 0

for venda in vendas:
    if venda >= meta:
        qtde += 1

total = len(vendas)                    # Total de vendas
porcentual = (qtde / total) * 100      # Calcula o percentual

print(f'O porcentual de pessoas que bateram a meta foi de {porcentual:.2f}%')