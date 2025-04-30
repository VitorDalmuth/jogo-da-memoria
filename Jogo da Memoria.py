"""
🧠 Jogo da Memória Visual Top
Versão: 1.1

Autores:
- Emilly Ruff
- Guilherme Izaias
- Giorgio Buka
- Gabriel Jabour
- Rafaela Martins Coelho
- Vitor Luis Dalmuth

Descrição:
Jogo da memória educativo com interface gráfica em Tkinter.
Cada par representa uma pergunta e resposta sobre estruturas de dados,
como pilha, fila, listas e listas 2D. O jogo alterna os turnos entre dois jogadores,
registra a pontuação e exibe o vencedor ao final.
Ideal para reforçar conceitos de estrutura de dados de forma interativa.
"""
import tkinter as tk
from tkinter import messagebox
import random
from collections import deque

pares_com_cores = [
    (("Qual estrutura adiciona no final e remove do início?", "Fila"), "#add8e6"),
    (("Qual estrutura só usa o topo para adicionar e remover?", "Pilha"), "#dda0dd"),
    (("Qual estrutura pode guardar elementos em ordem?", "Lista"), "#90ee90"),
    (("Qual estrutura é usada para criar grades como o tabuleiro?", "Lista 2D"), "#ffcccb"),
    (("Como é o comportamento da pilha?", "LIFO"), "#ffffcc"),
    (("Como é o comportamento da fila?", "FIFO"), "#ffb347")
]

pares = [p for (p, _) in pares_com_cores]
texto_para_cor = {texto: cor for (par, cor) in pares_com_cores for texto in par}
cartas = [item for par in pares for item in par]
random.shuffle(cartas)
tabuleiro = [cartas[i:i+4] for i in range(0, 12, 4)]
estado_tabuleiro = [['X'] * 4 for _ in range(3)]
widgets = [[None for _ in range(4)] for _ in range(3)]
pilha = []
turnos = deque(["Jogador1", "Jogador2"])
pontuacao = {"Jogador1": 0, "Jogador2": 0}

root = tk.Tk()
root.title("🧠 Jogo da Memória Visual Top")
root.geometry("960x540")
root.minsize(640, 360)

frame_superior = tk.Frame(root)
frame_superior.pack(fill=tk.X, pady=10)
info_label = tk.Label(frame_superior, text="", font=("Arial", 16))
info_label.pack()

frame_tabuleiro = tk.Frame(root)
frame_tabuleiro.pack(expand=True, fill=tk.BOTH)

def atualizar_info():
    placar = f"{pontuacao['Jogador1']} x {pontuacao['Jogador2']}"
    info_label.config(text=f"Turno de {turnos[0]}  |  Placar: {placar}")

def todos_revelados():
    return all('X' not in linha for linha in estado_tabuleiro)

def fim_de_jogo():
    j1, j2 = pontuacao["Jogador1"], pontuacao["Jogador2"]
    vencedor = "Empate! 🤝"
    if j1 > j2:
        vencedor = "Jogador1 venceu! 🏆"
    elif j2 > j1:
        vencedor = "Jogador2 venceu! 🏆"
    messagebox.showinfo("Fim do Jogo", f"Placar final: {j1} x {j2}\n{vencedor}")
    root.quit()

def esconder_cartas():
    for linha, coluna in pilha:
        widgets[linha][coluna].destroy()
        btn = criar_botao(linha, coluna)
        widgets[linha][coluna] = btn
        estado_tabuleiro[linha][coluna] = 'X'
    pilha.clear()

def verificar_par():
    (l1, c1), (l2, c2) = pilha
    t1 = tabuleiro[l1][c1]
    t2 = tabuleiro[l2][c2]
    par_correto = any((t1, t2) == p or (t2, t1) == p for p in pares)

    if par_correto:
        pontuacao[turnos[0]] += 1
        pilha.clear()
    else:
        turnos.rotate(-1)
        root.after(800, esconder_cartas)

    atualizar_info()
    if todos_revelados():
        fim_de_jogo()

def virar_carta(linha, coluna):
    if estado_tabuleiro[linha][coluna] != 'X' or len(pilha) == 2:
        return
    texto = tabuleiro[linha][coluna]
    estado_tabuleiro[linha][coluna] = texto
    widgets[linha][coluna].destroy()
    cor = texto_para_cor.get(texto, "#add8e6")

    lbl = tk.Label(frame_tabuleiro, text=texto, bg=cor, fg="black",
                   font=("Arial", 10, "bold"), wraplength=100, justify="center",
                   relief=tk.RAISED, borderwidth=2)
    lbl.grid(row=linha, column=coluna, sticky="nsew", padx=4, pady=4)
    widgets[linha][coluna] = lbl
    pilha.append((linha, coluna))
    if len(pilha) == 2:
        root.after(800, verificar_par)

def criar_botao(linha, coluna):
    b = tk.Button(frame_tabuleiro, text="", bg="gray", fg="black", relief=tk.RAISED,
                  font=("Arial", 10, "bold"), wraplength=100,
                  command=lambda l=linha, c=coluna: virar_carta(l, c))
    b.grid(row=linha, column=coluna, sticky="nsew", padx=4, pady=4)
    return b

for i in range(3):
    frame_tabuleiro.grid_rowconfigure(i, weight=1)
    for j in range(4):
        frame_tabuleiro.grid_columnconfigure(j, weight=1)
        widgets[i][j] = criar_botao(i, j)

atualizar_info()
root.mainloop()
