import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('D:/8semestr/Algorithms_and_models_for_data/lab12/lesmiserables.gml')

#позиціонування вузлів для візуалізації
pos = nx.spring_layout(G)

#налаштування розмірів та кольорів вузлів
node_sizes = [len(list(G.neighbors(node))) * 100 for node in G.nodes()]
node_colors = [G.degree(node) for node in G.nodes()]

#налаштування розмірів та кольорів ребер
edge_widths = [G[u][v]['value'] * 0.1 for u, v in G.edges()]

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, 
        font_size=10, font_color="black", edge_color="gray", width=edge_widths)
plt.title('Les Miserables Graph')
plt.show()
