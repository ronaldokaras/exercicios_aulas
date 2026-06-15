meses = [
'Janeiro',
'Fevereiro',
'Março',
'Abril',
'Maio',
'Junho',
'Julho',
'Agosto',
'Setembro',
'Outubro',
'Novembro',
'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

media_temperatura = sum(temperaturas) / len(temperaturas)

print(f"Média de temperatura: {media_temperatura:.2f}°C")

for i in range(len(meses)):
    if temperaturas[i] > media_temperatura:
        print(f"- {meses[i]}: {temperaturas[i]}°C")