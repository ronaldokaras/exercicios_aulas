nome = input("Seu nome: ")
email = input("Digite seu email: ")

if not nome or not email:
    print('Dados incorretos! Verifique')

elif '@' not in email or '.' not in email.split('@')[-1]:
    print('e-mail invalido!')
    
else:
    print(f'Cadastro realizado com sucesso!')
    print(f"Nome: {nome.title()}")
    print(f'E-mail: {email.lower()}')