import random

print("=== Jogo: Pedra, Papel e Tesoura ===\n")

jogando = True  # Controla se o jogo continua ou encerra

while jogando:

    # Validação da escolha do jogador
    while True:
        opcao = input("Escolha pedra, papel ou tesoura: ").lower().strip()
        if opcao in ["pedra", "papel", "tesoura"]:
            break
        print("Opção inválida! Tente novamente.")

    if opcao == "pedra":
        print("Você escolheu pedra!")
    elif opcao == "papel":
        print("Você escolheu papel!")
    else:
        print("Você escolheu tesoura!")

    maquina = random.choice(["pedra", "papel", "tesoura"])
    print("A máquina escolheu:", maquina)

    # Lógica do vencedor
    if opcao == maquina:
        print("Empate!")
    elif (opcao == "pedra" and maquina == "tesoura") or \
         (opcao == "papel" and maquina == "pedra") or \
         (opcao == "tesoura" and maquina == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    # Validação para continuar ou sair
    while True:
        # Corrigido: agora com \n (quebra de linha)
        jogar_novamente = input("\nDeseja jogar novamente? (sim/nao): ").lower().strip()
        
        if jogar_novamente in ["s", "sim"]:
            break  # Sai do loop de confirmação e inicia nova rodada
        elif jogar_novamente in ["n", "nao", "não"]:
            print("Até a próxima!")
            jogando = False  # Encerra o loop principal
            break
        else:
            print("Resposta inválida! Por favor, digite apenas 'sim' ou 'não'.")
            
    print()  # Linha em branco entre rodadas