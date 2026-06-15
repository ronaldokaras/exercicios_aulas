produto = input('Qual o produto? : ').strip()
categoria = input('Qual a categoria do produto? ').strip().lower()
qtde_str = input('Qual a quantidade atual do produto? ').strip()


if not produto or not categoria or not qtde_str:
    print('Preencha todas as informações!')
else:
    try:
        qtde = int(qtde_str) 
        
        if categoria == 'bebidas':
            if qtde < 75:
                print(f'Solicitar {produto} à equipe de compras, temos somente {qtde} unidades em estoque.')
                
        elif categoria == 'limpeza':
            if qtde < 30:
                print(f'Solicitar {produto} à equipe de compras, temos somente {qtde} unidades em estoque.')
                
        else:
            if qtde < 50:
                print(f'Solicitar {produto} à equipe de compras, temos somente {qtde} unidades em estoque.')
            else:
                print(f'{produto} está com estoque OK.')
                
    except ValueError:
        print('Erro: A quantidade deve ser um número inteiro!')