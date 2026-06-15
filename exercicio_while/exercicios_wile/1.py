while True:
    escolha = input('Escolha uma avaliação entre 0 e 10: ')
    
    if escolha.isdigit() and 0 <= int(escolha) <= 10:
        break
    
    print('Valor inválido. Digite um número entre 0 e 10.')
    
print(f'Você escolheu a avaliação {escolha}. Obrigado por participar!')