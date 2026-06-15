def calcular_percentual(votos, total):
    
    if total == 0:
        return 0.0
    return (votos / total) * 100


votos = [0] * 24

print("Enquete: Quem foi o melhor jogador?\n")


while True:
    try:
        entrada = int(input("Número do jogador (0=fim): "))
        if entrada == 0:
            break
        if 1 <= entrada <= 23:
            votos[entrada] += 1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
    except ValueError:
        print("Entrada inválida! Digite um número.")


total_votos = sum(votos[1:]) 


print("\nResultado da votação:\n")
print(f"Foram computados {total_votos} votos.\n")
print("Jogador Votos %")

melhor_jogador = 0
melhor_votos = 0


resultados = []

for i in range(1, 24):
    if votos[i] > 0:
        percentual = calcular_percentual(votos[i], total_votos)
        resultados.append((i, votos[i], percentual))
        
        if votos[i] > melhor_votos:
            melhor_votos = votos[i]
            melhor_jogador = i

for jogador, qtd, perc in resultados:
    print(f"{jogador} {qtd} {perc:.1f}%")


if melhor_jogador != 0:
    perc_melhor = calcular_percentual(melhor_votos, total_votos)
    print(f"\nO melhor jogador foi o número {melhor_jogador}, com {melhor_votos} votos, correspondendo a {perc_melhor:.1f}% do total de votos.")
else:
    print("\nNenhum voto válido foi computado.")
