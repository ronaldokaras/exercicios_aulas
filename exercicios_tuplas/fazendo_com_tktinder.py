from tkinter import *

def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()
    aluno = (nome, idade, curso)
    resultado.config(
    text=f"Nome: {aluno[0]}\nIdade: {aluno[1]}\nCurso: {aluno[2]}"
)
    
# Janela principal
janela = Tk()
janela.title("Cadastro de Aluno")
janela.geometry("300x250")
# Nome
Label(janela, text="Nome").pack()
entry_nome = Entry(janela)
entry_nome.pack()
# Idade
Label(janela, text="Idade").pack()
entry_idade = Entry(janela)
entry_idade.pack()
# Curso
Label(janela, text="Curso").pack()
entry_curso = Entry(janela)
entry_curso.pack()
# Botão
Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)
# Resultado
resultado = Label(janela, text="")
resultado.pack()
janela.mainloop()