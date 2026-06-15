cds = []

while True:
    nome = input('Digite o nome do CD (ou deixe em branco para terminar): ')
    if nome == '':
        break
    valor = float(input('Digite o valor do CD: R$ '))
    cds.append((nome, valor))

for nome, valor in cds:
    print(f"{nome}: R$ {valor:.2f}")

total = sum(valor for _, valor in cds)
print(f"\nTotal gasto: R$ {total:.2f}")