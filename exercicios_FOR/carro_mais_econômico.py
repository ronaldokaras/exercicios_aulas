# Dados pré-definidos para teste rápido
modelos = ['fusca', 'gol', 'uno', 'vectra', 'peugeout']
consumos = [7.0, 10.0, 12.5, 9.0, 14.5]

preco_gasolina = 2.25
distancia = 1000

# Encontrar mais econômico
indice_mais_economico = consumos.index(max(consumos))
modelo_mais_economico = modelos[indice_mais_economico]

for i in range(5):
    litros = distancia / consumos[i]
    custo = litros * preco_gasolina
    print(f"{i+1} - {modelos[i]} - {consumos[i]:.1f} - {litros:.1f} litros - R$ {custo:.2f}")

print(f"O menor consumo é do {modelo_mais_economico}.")



























