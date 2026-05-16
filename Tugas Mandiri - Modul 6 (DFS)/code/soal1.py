import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "F"),
    ("C", "G")
])
print("Urutan DFS tanpa batas:")
for edge in nx.dfs_edges(G, source="A"):
    print(edge)
print("\nUrutan DFS dengan depth_limit=2:")
for edge in nx.dfs_edges(G, source="A", depth_limit=2):
    print(edge)
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(6, 4))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=12
)
