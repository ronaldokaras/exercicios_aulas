vendas = [941,852, 753, 654, 555, 456, 357, 258, 159, 50, 386, 371,294, 205, 116, 27, 938, 849, 760, 671, 582, 493, 404, 315, 226, 137]

vendedores = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Luiza', 'Rafael', 'Fernanda', 'Gustavo', 'Isabela', 'Bruno', 'Camila', 'Ricardo', 'Sofia', 'Felipe', 'Larissa', 'André', 'Mariana', 'Thiago', 'Juliana', 'Eduardo', 'Aline', 'Vitor', 'Carla', 'Diego']

meta = 50
i = 0

while vendas[i] > meta:
    print(f'{vendedores[i]} bateu a meta de vendas com {vendas[i]} unidades vendidas\n')
    i += 1
