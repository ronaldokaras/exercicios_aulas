# ===================== LOCADORA DE FILMES =====================

filmes = {
    1: ("Guardiões da Galáxia", 10.99),
    2: ("Avatar", 8.90),
    3: ("Rio", 6.90),
    4: ("O Rei Leão", 7.50),
    5: ("Vingadores: Ultimato", 12.99)
}

def mostrar_filmes():
    if not filmes:
        print("\nNenhum filme cadastrado.")
        return
    print("\nFILMES DISPONÍVEIS:")
    print("-" * 60)
    for id_filme, (nome, preco) in filmes.items():
        print(f"{id_filme:2d} -> {nome:30} R$ {preco:.2f}")
    print("-" * 60)

def adicionar_filme():
    print("\n ADICIONAR NOVO FILME")
    nome = input("Digite o nome do filme: ").strip()
    
    if not nome:
        print("Nome não pode ser vazio!")
        return
    
    try:
        preco = float(input("Digite o preço (ex: 9.90): R$ "))
        if preco <= 0:
            print("Preço deve ser maior que zero!")
            return
    except ValueError:
        print("Preço inválido!")
        return
    
    novo_id = max(filmes.keys()) + 1 if filmes else 1
    filmes[novo_id] = (nome, preco)
    print(f" Filme '{nome}' adicionado com sucesso! ID: {novo_id}")

def remover_filme():
    if not filmes:
        print(" Não há filmes para remover.")
        return
    
    mostrar_filmes()
    try:
        id_remover = int(input("\nDigite o ID do filme que deseja remover: "))
        
        if id_remover in filmes:
            nome = filmes[id_remover][0]
            confirmacao = input(f"Tem certeza que deseja remover '{nome}'? (s/n): ").strip().lower()
            
            if confirmacao == 's':
                del filmes[id_remover]
                print(f" Filme '{nome}' removido com sucesso!")
            else:
                print("Operação cancelada.")
        else:
            print(" ID não encontrado!")
    except ValueError:
        print(" Digite um número válido!")

def locadora():
    total_compra = 0.0
    carrinho = []

    print("=" * 65)
    print("BEM-VINDO À LOCADORA DE FILMES ")
    print("=" * 65)

    while True:
        print("\n" + "="*65)
        print("1  Alugar filme")
        print("2  Ver filmes disponíveis")
        print("3  Adicionar novo filme")
        print("4  Remover filme")
        print("0  Finalizar compra e sair")
        print("="*65)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                break
            elif opcao == 1:
                mostrar_filmes()
                if filmes:
                    escolha = int(input("\nDigite o ID do filme que deseja alugar: "))
                    if escolha in filmes:
                        nome, valor = filmes[escolha]
                        carrinho.append(nome)
                        total_compra += valor
                        print(f" Adicionado: '{nome}' - R$ {valor:.2f}")
                    else:
                        print("ID não encontrado!")
            elif opcao == 2:  
                mostrar_filmes()
            elif opcao == 3:   
                adicionar_filme()
            elif opcao == 4:   
                remover_filme()
            else:
                print(" Opção inválida!")
                
        except ValueError:
            print(" Por favor, digite um número válido.")

    print("\n" + "=" * 65)
    print("COMPRA FINALIZADA!")
    print("=" * 65)
    
    if carrinho:
        print(" Filmes alugados:")
        for i, filme in enumerate(carrinho, 1):
            print(f"   {i}. {filme}")
        print("-" * 65)
        print(f" VALOR TOTAL: R$ {total_compra:.2f}")
    else:
        print("Nenhum filme foi alugado.")
    
    print("=" * 65)

if __name__ == "__main__":
    locadora()