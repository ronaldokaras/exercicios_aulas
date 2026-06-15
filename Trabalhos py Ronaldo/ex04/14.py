tamanho_dowload = float(input("Digite o tamanho  do arquivo em MB : "))
velocidade_internet = float(input("Digite a velocidade da internet em Mbps : "))


megabit = tamanho_dowload * 8

segundo = megabit / velocidade_internet

minutos = segundo / 60



print(f"Tantos minutos para o dowload: {minutos:.2f} " )