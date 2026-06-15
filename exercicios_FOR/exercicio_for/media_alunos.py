alunos = ['José', 'Maria', 'João', 'Ana', 'Carlos', 'Fernanda', 'Paulo', 'Mariana', 'Ricardo', 'Sofia']

notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

alunos_aprovados = []  # Lista vazia fora do loop

for i in range(len(alunos)):
    media = sum(notas[i]) / len(notas[i])
    aprovado = media >= 7
    
    if aprovado:
        print(f"Aluno: {alunos[i]}, Média: {media:.2f}")
        alunos_aprovados.append(alunos[i])  # Adiciona à lista

print(f"A quantidade de alunos aprovados foi de: {len(alunos_aprovados)}")