meta = 0.05 
rendimento = 0.25

investimento = float(input("DIGITE SEU INVETIMENTO: "))

if investimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print("A taxa foi de {}".format(taxa))
    else:
        taxa = 0.02
        print("A taxa foi de {}".format(taxa))
else:
    taxa = 0 
    print("A taxa foi de {}".format(taxa))