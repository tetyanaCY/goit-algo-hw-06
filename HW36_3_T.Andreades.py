import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (перехресть)
G.add_node("A")  # Перехрестя A
G.add_node("B")  # Перехрестя B
G.add_node("C")  # Перехрестя C
G.add_node("D")  # Перехрестя D
G.add_node("E")  # Перехрестя E

# Додавання ребер (вулиць)
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "C")
G.add_edge("B", "D")
G.add_edge("C", "D")
G.add_edge("C", "E")
G.add_edge("D", "E")

# Проведення DFS (пошуку в глибину)
dfs_edges = list(nx.dfs_edges(G, source="A"))

# Проведення BFS (пошуку в ширину)
bfs_edges = list(nx.bfs_edges(G, source="A"))

dfs_edges, bfs_edges


# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=2, font_size=15)
plt.title("Транспортна мережа міста")
plt.show()
# Аналіз основних характеристик графа

# Кількість вершин
number_of_nodes = G.number_of_nodes()

# Кількість ребер
number_of_edges = G.number_of_edges()

# Ступінь кожної вершини
degrees = G.degree()

# Виведення результатів
number_of_nodes, number_of_edges, list(degrees)
# Використання алгоритму Дейкстри для знаходження найкоротшого шляху між усіма парами вершин
for source in G.nodes():
    for target in G.nodes():
        if source != target:
            shortest_path = nx.dijkstra_path(G, source, target)
            print(f"Найкоротший шлях з {source} до {target}: {shortest_path}")
# Формування та виведення результатів
print(f"Кількість вершин (перехресть): {number_of_nodes}")
print(f"Кількість ребер (вулиць): {number_of_edges}")
print("Ступінь кожної вершини (кількість вулиць, що з'єднуються з кожним перехрестям):")

for node, degree in degrees:
    print(f"Перехрестя {node}: {degree} вулиці{'я' if degree == 1 else '' if degree < 5 else 'ь'}")
    # Використання того ж графа, що і в першому завданні
