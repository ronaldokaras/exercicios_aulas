import random
from datetime import datetime

registro = random.randint(1000, 9999)
data = datetime.now().strftime("%d/%m/%Y")

print('=' * 50)
print(f'           REGISTRO DE COMPRA Nº {registro}')
print(f'                   {data}')
print('=' * 50)

cliente = input("Nome do cliente: ")
produto = input("Produto: ")
quantidade = int(input("Quantidade: "))
preco_unitario = float(input("Preço unitário (R$): "))

subtotal = quantidade * preco_unitario

print('\n' + '-' * 50)
print("RECIBO:")
print(f"Cliente: {cliente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total: R$ {subtotal:.2f}")
print('-' * 50)
print(f"Registro Nº {registro} - {data}")
print('=' * 50)