vendas_produtos = [
    ('iphone', 558147, 951642), 
    ('galaxy', 712350, 244295),                    
    ('ipad', 573823, 26964),                    
    ('tv', 405252, 787604),                     
    ('máquina de café', 718654, 867660),                   
    ('kindle', 531580, 78830), 
    ('geladeira', 973139, 710331), 
    ('adega', 892292, 646016),
    ('notebook dell', 422760, 694913), 
    ('notebook hp', 154753, 539704), 
    ('notebook asus', 887061, 324831), 
    ('microsoft surface', 438508, 667179), 
    ('webcam', 237467, 295633), 
    ('caixa de som', 489705, 725316), 
    ('microfone', 328311, 644622),
    ('câmera canon', 591120, 994303)
]

# Encontrar produto mais vendido em 2020
mais_vendido = max(vendas_produtos, key=lambda x: x[2])
print(f'Produto mais vendido em 2020: {mais_vendido[0]} com {mais_vendido[2]} unidades')

# Calcular diferença percentual de cada produto
for nome, v2019, v2020 in vendas_produtos:
    diferenca = (v2020 / v2019 - 1) * 100
    if diferenca > 0:
        print(f'{nome}: Ano 2020 maior em {diferenca:.1f}%')
    elif diferenca < 0:
        print(f'{nome}: Ano 2019 maior em {-diferenca:.1f}%')
    else:
        print(f'{nome}: Vendas iguais')

#========== ou ====

for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020 / vendas2019 - 1
        print(f"{produto} teve {vendas2019} em 2019 ")
        print(f"{produto} teve {vendas2020} em 2020 ")
        print(f"Com crescimento de {crescimento:.1%} ")