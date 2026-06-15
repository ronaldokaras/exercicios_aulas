while True:
    idades = [] 
    
    for i in range(1, 6):
        valor = int(input(f"Idade da pessoa {i}: "))
        idades.append(valor)
        
    total = sum(idades)
    jovens = sum(1 for idade in idades if 0 <= idade <= 25)
    seniores = sum(1 for idade in idades if 26 <= idade <= 60)
    idosas = sum(1 for idade in idades if idade > 60)

    media = total / 5

    print(f"Total de pessoas: {len(idades)}")
    print(f"Pessoas jovens (0-25 anos): {jovens}")
    print(f"Pessoas sêniores (26-60 anos): {seniores}")
    print(f"Pessoas idosas (mais de 60 anos): {idosas}")
    print(f'Esta equipe tem uma média de idade de {media:.0f} anos. E é considerada uma equipe {"jovem" if media <= 25 else "sênior" if media <= 60 else "idosa"}.')

    break

