total = int(input("Número total de eleitores: "))

votos_Lula = 0
votos_Bolsonaro = 0
votos_Renan = 0

for i in range(1, total + 1):
    voto = int(input(f"Eleitor {i} - Vote (1=Lula, 2=Bolsonaro, 3=Renan Santos): "))
    
    if voto == 1:
        votos_Lula += 1
    elif voto == 2:
        votos_Bolsonaro += 1
    elif voto == 3:
        votos_Renan += 1

print(f"Lula:         {votos_Lula} votos")
print(f"Bolsonaro:    {votos_Bolsonaro} votos")
print(f"Renan Santos: {votos_Renan} votos")

if votos_Lula > votos_Bolsonaro and votos_Lula > votos_Renan:
    print(f"\nO vencedor é: Lula")
elif votos_Bolsonaro > votos_Lula and votos_Bolsonaro > votos_Renan:
    print(f"\nO vencedor é: Bolsonaro")
elif votos_Renan > votos_Lula and votos_Renan > votos_Bolsonaro:
    print(f"\nO vencedor é: Renan Santos")
else:
    print("\nEmpate!")