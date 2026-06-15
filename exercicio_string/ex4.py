nome = input("Seu nome: ").strip()
email = input("Digite seu email: ").strip()

if len(nome) == 0 or len(email) == 0:
    print('preencha nome e email. ')

elif email.find('@') == -1:
    print('e-mail invalido! falta o @')

elif email.find('.', email.find('@')) == -1:
    print('e-mail invalido! depois do @ deve ter um ponto (.).')

else:
    print('Cadastro realizado com sucesso!')