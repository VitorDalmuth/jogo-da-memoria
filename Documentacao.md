
# 🧠 Jogo da Memória Visual Top

### Versão: 1.1  
### Autores:
- Emilly Ruff  
- Guilherme Izaias  
- Giorgio Buka  
- Gabriel Jabour  
- Rafaela Martins Coelho  
- Vitor Luis Dalmuth  

---

## 📘 Descrição Geral

Este projeto é um **jogo da memória educativo** desenvolvido em Python com interface gráfica usando Tkinter. O jogo é voltado para dois jogadores e tem como objetivo principal **reforçar o aprendizado das estruturas de dados**: **Pilha**, **Fila** e **Lista**, através de uma dinâmica lúdica e interativa.

---

## 🃏 Jogo da Memória (Matching Game)

### 👥 Jogadores:
Dois jogadores se revezam tentando encontrar pares de cartas relacionados a perguntas e respostas sobre estruturas de dados.

### 🎯 Objetivo:
Encontrar mais pares corretos do que o oponente até que todas as cartas tenham sido reveladas.

---

## 📦 Como são usadas as Estruturas de Dados

### ✅ Fila — Controle de Turnos

- Usada para gerenciar a vez de cada jogador.
- Implementada com `collections.deque`.

**Exemplo:**
```python
turnos = deque(["Jogador1", "Jogador2"])
```

- A cada jogada, se o jogador errar, ele vai para o fim da fila:

```python
turnos.rotate(-1)
```

---

### ✅ Pilha — Cartas Viradas

- Armazena as **duas cartas viradas na rodada atual**.
- Após virar duas cartas:
  - Se forem pares → o jogador pontua.
  - Se não → as cartas são "desviradas".

**Exemplo:**
```python
pilha = []
pilha.append((linha, coluna))  # adicionar carta virada
```

---

### ✅ Lista — Tabuleiro

- Representa as cartas embaralhadas no jogo.
- Implementada como **lista 2D** (`3x4`).

**Exemplo:**
```python
tabuleiro = [
  ["Pilha", "Lista", "Fila", "FIFO"],
  ...
]
```

- Também é usada para guardar os botões da interface (`widgets`) e o estado atual das cartas (`estado_tabuleiro`).

---

## 🖥️ Tecnologias Utilizadas

- Python 3
- Tkinter (GUI nativa)
- `random.shuffle()` para embaralhar as cartas
- `collections.deque` para controle de fila (turnos)

---

## 🧮 Regras de Funcionamento

1. O jogo inicia com 12 cartas (6 pares embaralhados).
2. Jogadores se revezam clicando em duas cartas por vez.
3. Se as cartas formarem um par válido (pergunta e resposta), elas permanecem abertas e o jogador ganha ponto.
4. Caso contrário, as cartas são viradas novamente e o turno passa ao outro jogador.
5. O jogo termina quando todas as cartas forem reveladas.
6. Uma mensagem é exibida com o **vencedor** e o **placar final**.

---

## ▶️ Como Executar

### Pré-requisitos:

- Python 3 instalado
- Tkinter habilitado (já incluso nas versões oficiais do Python em macOS/Windows)

### Comandos:

```bash
# Criação do ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # no macOS/Linux

# Instalar dependência
pip install tk

# Executar o jogo
python "Jogo da Memoria.py"
```

---

## 📁 Estrutura de Arquivos

```bash
Jogo da Memoria/
├── Jogo da Memoria.py
├── README.md
├── requirements.txt
└── .venv/ (opcional - ambiente virtual)
```

---

## 🧠 Conclusão

Este projeto integra o conteúdo teórico de estruturas de dados com uma aplicação prática em Python. Ele demonstra claramente o uso de **Pilha, Fila e Lista** em um contexto lúdico, colaborativo e visual.
---

## ✅ requirements.txt

```txt
tk
```
