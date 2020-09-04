import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors

G = nx.gnr_graph(50, 0.14)

# check how many times a given degree occurs:
degrees = [G.in_degree[a] for a in G.nodes]
# norm_degree_dict for saving the spaces in y axis:
norm_degree_dict = dict(zip(set(degrees), np.arange(max(degrees))))
max_d = max(norm_degree_dict.values())
# generate unique x-coordinates. divide by 2 for zero-centering:
degrees = {degree: [a for a in degrees.count(degree) / 2. - np.arange(degrees.count(degree))] for degree in
           set(degrees)}
color_map = dict(zip(degrees.keys(), [(i / (len(degrees))) for i in range((len(degrees)))]))
# build positioning dictionary:
positions = {a: (degrees[G.in_degree[a]].pop(), max_d - norm_degree_dict[G.in_degree[a]]) for a in G.nodes}
colors = [color_map[G.in_degree[a]] for a in G.nodes]

sc = nx.draw_networkx_nodes(G=G, pos=positions, node_list=G.nodes(), alpha=0.9,
                            node_size=220, node_color=colors)

nx.draw_networkx_edges(G=G, pos=positions, edge_color='k', alpha=0.9, width=3)
# sc.set_norm(mcolors.LogNorm())
# nx.draw(G, with_labels=False, font_weight='bold', node_size = 20 ,pos=positions, node_color=colors)
# plt.savefig("graph.svg")
plt.show()
i = 9
