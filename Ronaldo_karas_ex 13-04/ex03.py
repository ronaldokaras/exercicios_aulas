print("="* 50)

estado = input("DIGITE SEU ESTADO C para casado, S para solteiro, V para viúvo, O para outros: ")

if estado == "C".lower():
    print("CASADO")
elif estado == "S".lower():
    print("SOLTEIRO")
elif estado == "V".lower():
    print("VUIVO")
elif estado == "O".lower():
    print("OUTROS")
else:
    print("Opção invalida")