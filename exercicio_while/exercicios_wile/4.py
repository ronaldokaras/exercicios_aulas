while True:
    try:
        a = float(input("População inicial A: "))
        b = float(input("População inicial B: "))
        taxa_a = float(input("Taxa de crescimento A (%): ")) / 100
        taxa_b = float(input("Taxa de crescimento B (%): ")) / 100
        
        if a <= 0 or b <= 0:
            print("Populações devem ser maiores que zero!")
            continue
            
    except:
        print("Erro: Digite apenas números!")
        continue

    anos = 0
    while a < b and anos < 1000:
        a = round(a * (1 + taxa_a))
        b = round(b * (1 + taxa_b))
        anos += 1

    if anos >= 1000:
        print("Não foi possível calcular (verifique as taxas).")
    else:
        print(f"\nSerão necessários {anos} anos.")
        print(f"População final A: {a:,.0f}")
        print(f"População final B: {b:,.0f}")

    repetir = input("\nDeseja fazer outro cálculo? (S/N): ").strip().upper()
    if repetir != "S":
        print("Programa encerrado.")
        break