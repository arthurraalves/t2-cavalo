# Trabalho Prático 2 - Grafo do Cavalo (3x3)

## 📌 Descrição

Este projeto implementa o grafo dos movimentos do cavalo em um tabuleiro de xadrez 3x3.

Cada posição do tabuleiro é representada como um vértice, e existe uma aresta entre dois vértices quando o cavalo pode se mover entre eles.

## 🔢 Numeração dos vértices

A numeração segue a ordem de leitura:

0 1 2
3 4 5
6 7 8

## 🔗 Arestas do grafo

As arestas foram construídas manualmente com base nos movimentos válidos do cavalo:

0-5, 0-7
1-6, 1-8
2-3, 2-7
3-8
5-6

O vértice 4 é isolado, pois não possui movimentos válidos.

## ⚙️ Funcionalidades

O programa realiza:

* Impressão da lista de adjacência
* Identificação das componentes conexas
* Cálculo da menor distância entre dois vértices (BFS)
* Verificação de existência de ciclo
* Exibição de um ciclo encontrado

## ▶️ Como executar

1. Entre na pasta `src`
2. Execute:

```bash
python main.py
```

## 📊 Resultados esperados

* Componentes conexas: 2
* Distância mínima entre 0 e 8: 4
* O grafo possui ciclo

## 📚 Complexidade

* BFS/DFS: O(V + E)
* Espaço: O(V)
