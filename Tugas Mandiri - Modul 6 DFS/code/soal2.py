import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("E", "F")
])
start = "A"
goal = "F"

dfs_edges = list(nx.dfs_edges(G, source=start))
print("Urutan DFS:")
for edge in dfs_edges:
    print(edge)
visited_nodes = [start]

for edge in dfs_edges:
    visited_nodes.append(edge[1])
    if edge[1] == goal:
        break
print("\nUrutan traversal sampai goal ditemukan:")
for node in visited_nodes:
    print(node)
if goal in visited_nodes:
    print(f"\nGoal {goal} ditemukan menggunakan DFS")
else:
    print(f"\nGoal {goal} tidak ditemukan menggunakan DFS")
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(6, 4))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=12,
    arrows=True
)
