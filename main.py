import matplotlib.pyplot as plt
import numpy as np
from Algorithm.Astar import Astar
from Algorithm.BFS import BFS
from Heuristics.Heuristica import Heuristic1, Heuristic2
from Problem.Jogo8.Complexidade import Complexidade
from Problem.Jogo8.Jogo8 import Jogo8

# Solicitar dados do usuário
tamanho = int(input("Digite o tamanho do tabuleiro (por exemplo, 3 para um tabuleiro 3x3): "))
complexidade = int(input("Digite o nível de complexidade (1 para Fácil, 2 para Médio, 3 para Difícil): "))

# Mapear a entrada de complexidade para o valor correto
if complexidade == 1:
    c = Complexidade.Facil
elif complexidade == 2:
    c = Complexidade.Medio
elif complexidade == 3:
    c = Complexidade.Dificil
else:
    print("Nível de complexidade inválido. Usando 'Difícil' por padrão.")
    c = Complexidade.Dificil

# Listas para armazenar os resultados
custos_distancia_quarteirao = []
tempos_distancia_quarteirao = []
estados_distancia_quarteirao = []
custos_pecas_fora_lugar = []
tempos_pecas_fora_lugar = []
estados_pecas_fora_lugar = []
custos_bfs = []
tempos_bfs = []
estados_bfs = []

# Coleta de dados
for _ in range(50):
    instancia = Jogo8(tamanho, c)

    algoritmos = [
        ('A* - Distância de quarteirão', Astar(instancia.estado_inicial, instancia.estado_final, Heuristic2(instancia.estado_final))),
        ('A* - Quantidade de peças fora do lugar', Astar(instancia.estado_inicial, instancia.estado_final, Heuristic1(instancia.estado_final))),
        ('BFS', BFS(instancia.estado_inicial, instancia.estado_final))
    ]

    for nome, alg in algoritmos:
        alg.encontrar_solucao()
        custo = len(alg.solucao)
        tempo = alg.tempo_execucao
        estados = alg.estados_analisados

        if nome == 'A* - Distância de quarteirão':
            custos_distancia_quarteirao.append(custo)
            tempos_distancia_quarteirao.append(tempo)
            estados_distancia_quarteirao.append(estados)
        elif nome == 'A* - Quantidade de peças fora do lugar':
            custos_pecas_fora_lugar.append(custo)
            tempos_pecas_fora_lugar.append(tempo)
            estados_pecas_fora_lugar.append(estados)
        elif nome == 'BFS':
            custos_bfs.append(custo)
            tempos_bfs.append(tempo)
            estados_bfs.append(estados)

# Verificar os comprimentos das listas
print(f"Comprimento dos dados para A* - Distância de quarteirão: {len(custos_distancia_quarteirao)}, {len(tempos_distancia_quarteirao)}, {len(estados_distancia_quarteirao)}")
print(f"Comprimento dos dados para A* - Quantidade de peças fora do lugar: {len(custos_pecas_fora_lugar)}, {len(tempos_pecas_fora_lugar)}, {len(estados_pecas_fora_lugar)}")
print(f"Comprimento dos dados para BFS: {len(custos_bfs)}, {len(tempos_bfs)}, {len(estados_bfs)}")

# Criação do gráfico
plt.figure(figsize=(12, 6))

# Plotar tempo de execução
plt.subplot(1, 2, 1)
if len(custos_distancia_quarteirao) == len(tempos_distancia_quarteirao):
    plt.plot(custos_distancia_quarteirao, tempos_distancia_quarteirao, 'r-', label='A* - Distância de quarteirão')
if len(custos_pecas_fora_lugar) == len(tempos_pecas_fora_lugar):
    plt.plot(custos_pecas_fora_lugar, tempos_pecas_fora_lugar, 'g-', label='A* - Quantidade de peças fora do lugar')
if len(custos_bfs) == len(tempos_bfs):
    plt.plot(custos_bfs, tempos_bfs, 'b-', label='BFS')
plt.yscale('log', base=2)
plt.xlabel('Custo da Solução Ótima')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução vs. Custo da Solução Ótima')
plt.legend()

# Plotar quantidade de estados analisados
plt.subplot(1, 2, 2)
if len(custos_distancia_quarteirao) == len(estados_distancia_quarteirao):
    plt.plot(custos_distancia_quarteirao, estados_distancia_quarteirao, 'r-', label='A* - Distância de quarteirão')
if len(custos_pecas_fora_lugar) == len(estados_pecas_fora_lugar):
    plt.plot(custos_pecas_fora_lugar, estados_pecas_fora_lugar, 'g-', label='A* - Quantidade de peças fora do lugar')
if len(custos_bfs) == len(estados_bfs):
    plt.plot(custos_bfs, estados_bfs, 'b-', label='BFS')
plt.yscale('log', base=2)
plt.xlabel('Custo da Solução Ótima')
plt.ylabel('Quantidade de Estados Analisados')
plt.title('Quantidade de Estados Analisados vs. Custo da Solução Ótima')
plt.legend()

plt.tight_layout()
plt.savefig('resultados.png')
plt.show()
