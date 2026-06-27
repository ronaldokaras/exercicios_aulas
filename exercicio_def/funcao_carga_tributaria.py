def carga_tributaria(preco,custo,lucro):
    imposto = preco - custo - lucro
    return imposto / preco

preco = 1500
custo = 400
lucro = 800

print(f"A carga tributaria foi de {carga_tributaria(preco,custo,lucro):.1%} ")