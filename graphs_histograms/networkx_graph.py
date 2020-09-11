import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import itertools
from matplotlib import colors as mcolors
from collections import Counter

def draw_graph_path(edge_file,selected_nodes):
    selected_edges = set([(x[0],x[1]) for x in zip(selected_nodes[:-1],selected_nodes[1:])])
    G, color_map, positions, y_pos_dict = create_graph_locations(edge_file)

    colors = ['b' if a in selected_nodes else 'grey' for a in G.nodes]
    sc = nx.draw_networkx_nodes(G=G, pos=positions, node_list=G.nodes(), alpha=0.9,
                                node_size=120, node_color=colors)
    edge_colors = ['b' if a in selected_edges else 'grey' for a in G.edges]
    edge_width = [4 if a in selected_edges else 2 for a in G.edges]
    nx.draw_networkx_edges(G=G, pos=positions, edge_color=edge_colors, alpha=0.9, width=edge_width)

    labels = dict(zip(selected_nodes, selected_nodes))
    nx.draw_networkx_labels(G,pos=positions,labels=labels,font_size=12,font_color='r',font_weight = 'bold')
    plt.title('->'.join(selected_nodes))
    plt.show()


def draw_color_graph(edge_file):
    G, color_map, positions, y_pos_dict = create_graph_locations(edge_file)

    #list of colors according to the nodes
    colors = [color_map[y_pos_dict[a]] for a in G.nodes]
    sc = nx.draw_networkx_nodes(G=G, pos=positions, node_list=G.nodes(), alpha=0.9,
                                node_size=120, node_color=colors)
    nx.draw_networkx_edges(G=G, pos=positions, edge_color='gray', alpha=0.9, width=4)
    # plt.savefig("graph.svg")
    plt.title('->'.join(['The', 'Graph']))
    plt.show()


def create_graph_locations(edge_file):
    G = nx.read_edgelist(edge_file, delimiter=",", data=(("weight", float),), create_using=nx.DiGraph())
    # file weight are node y positions:
    list_tuples_y_pos = [[(u, int(G[u][v]['weight'])), (v, int(G[u][v]['weight'] + 1))] for u, v in G.edges()]
    y_pos_dict = dict(itertools.chain(*list_tuples_y_pos))
    y_pos_value_list = list(y_pos_dict.values())
    max_y_pos = max(y_pos_value_list)
    yx_position_dict = {
    degree: [a for a in y_pos_value_list.count(degree) / 2. - np.arange(y_pos_value_list.count(degree))]
    for degree in set(y_pos_value_list)}
    # color dict - for every y pos get relevant color:
    color_map = dict(
        zip(yx_position_dict.keys(), [(i / (len(yx_position_dict))) for i in range((len(yx_position_dict)))]))
    # create final pos dict: {node:(x,y)}
    positions = {a: (yx_position_dict[y_pos_dict[a]].pop(), max_y_pos - y_pos_dict[a]) for a in G.nodes}
    return G, color_map, positions, y_pos_dict


if __name__ =='__main__':
    # draw_color_graph("taxon_file.txt")
    draw_graph_path("taxon_file.txt",['Viruses','Asfarviridae','Asfivirus'])