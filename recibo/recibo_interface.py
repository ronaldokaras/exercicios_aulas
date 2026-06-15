import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import datetime

# Gera número de registro e data
registro = random.randint(1000, 9999)
data = datetime.now().strftime("%d/%m/%Y")

def gerar_recibo():
    # Pega os valores dos campos
    cliente = entry_cliente.get().strip()
    produto = entry_produto.get().strip()
    quantidade = entry_qtd.get().strip()
    preco = entry_preco.get().strip().replace(',', '.')
    
    # Validações
    if not cliente or not produto or not quantidade or not preco:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    if not quantidade.isdigit() or int(quantidade) <= 0:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo!")
        return
    
    try:
        preco_num = float(preco)
        if preco_num <= 0:
            raise ValueError
    except:
        messagebox.showerror("Erro", "Preço unitário inválido!")
        return
    
    qtd_num = int(quantidade)
    total = qtd_num * preco_num
    
    # Monta o texto do recibo
    recibo = f"""
{'='*50}
       REGISTRO DE COMPRA Nº {registro}
                 {data}
{'='*50}

Cliente: {cliente}
Produto: {produto}
Quantidade: {qtd_num}
Preço unitário: R$ {preco_num:.2f}
Total: R$ {total:.2f}

{'-'*50}
Registro Nº {registro} - {data}
{'='*50}
"""
    # Exibe no widget Text
    text_recibo.delete(1.0, tk.END)
    text_recibo.insert(tk.END, recibo)
    
    # Salva em arquivo
    with open(f"registro_{registro}.txt", "w", encoding="utf-8") as f:
        f.write(recibo)
    
    messagebox.showinfo("Sucesso", f"Recibo salvo como 'registro_{registro}.txt'")

# Cria a janela principal
janela = tk.Tk()
janela.title("Sistema de Registro de Compra")
janela.geometry("550x620")
janela.configure(bg="#f0f0f0")

# Estilos
fonte_titulo = ("Arial", 12, "bold")
fonte_campos = ("Arial", 10)

# Cabeçalho
frame_cabecalho = tk.Frame(janela, bg="#2c3e50", height=80)
frame_cabecalho.pack(fill=tk.X)
tk.Label(frame_cabecalho, text=f"REGISTRO DE COMPRA Nº {registro}", 
         font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=(10,0))
tk.Label(frame_cabecalho, text=data, font=("Arial", 10), fg="#ecf0f1", bg="#2c3e50").pack()

# Formulário
frame_form = tk.LabelFrame(janela, text="Dados da Compra", font=fonte_titulo, bg="#ffffff", padx=10, pady=10)
frame_form.pack(pady=15, padx=20, fill=tk.X)

# Linha 0 - Cliente
tk.Label(frame_form, text="Cliente:", font=fonte_campos, bg="#ffffff").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_cliente = tk.Entry(frame_form, width=40, font=fonte_campos)
entry_cliente.grid(row=0, column=1, pady=5, padx=5)

# Linha 1 - Produto
tk.Label(frame_form, text="Produto:", font=fonte_campos, bg="#ffffff").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_produto = tk.Entry(frame_form, width=40, font=fonte_campos)
entry_produto.grid(row=1, column=1, pady=5, padx=5)

# Linha 2 - Quantidade
tk.Label(frame_form, text="Quantidade:", font=fonte_campos, bg="#ffffff").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_qtd = tk.Entry(frame_form, width=20, font=fonte_campos)
entry_qtd.grid(row=2, column=1, sticky=tk.W, pady=5, padx=5)

# Linha 3 - Preço unitário
tk.Label(frame_form, text="Preço unitário (R$):", font=fonte_campos, bg="#ffffff").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_preco = tk.Entry(frame_form, width=20, font=fonte_campos)
entry_preco.grid(row=3, column=1, sticky=tk.W, pady=5, padx=5)

# Botão
btn_gerar = tk.Button(janela, text="GERAR RECIBO", command=gerar_recibo,
                      bg="#27ae60", fg="white", font=("Arial", 11, "bold"),
                      padx=20, pady=8, relief=tk.RAISED, bd=2)
btn_gerar.pack(pady=10)

# Área do recibo
frame_recibo = tk.LabelFrame(janela, text="RECIBO", font=fonte_titulo, bg="#ffffff", padx=10, pady=10)
frame_recibo.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

text_recibo = tk.Text(frame_recibo, height=12, wrap=tk.WORD, font=("Courier", 9), bg="#fef9e6")
text_recibo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_recibo, orient=tk.VERTICAL, command=text_recibo.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_recibo.config(yscrollcommand=scrollbar.set)

# Inicia a aplicação
janela.mainloop()