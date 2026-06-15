print("="* 50)

turno = input("DIGITE SEU ESTADO M para MATUTINO, V para VESPERTINO, N para NOTURNO: ").lower()

if turno == "m":
    print("BOM DIA")
elif turno == "v":
    print("BOA TARDE")
elif turno == "n":
    print("BOA NOITE")
else:
    print("Opção invalida")