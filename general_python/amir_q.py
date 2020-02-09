from collections import defaultdict
import math
import os
import random
import re
import sys



def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    val = val - 1

    adj_dict = dict()
    for s, t in zip(graph_from, graph_to):
        adj_dict.setdefault(s - 1, set()).add(t - 1)

    same_color_nodes = set(
        map(lambda x: x[0], list(filter(lambda x: x[1] == ids[val] and x[0] != val, zip(range(graph_nodes), ids)))))

    if len(same_color_nodes) == 0:
        return -1
    path_len = 1
    for _ in range(graph_nodes):
        if adj_dict[val].intersection(same_color_nodes):
            return path_len
        new_adj_dict = dict()
        for n in adj_dict:
            new_adj_dict[n] = new_adj_dict.setdefault(s, set()).union(adj_dict[n])
        adj_dict = new_adj_dict
        path_len += 1
    return path_len




# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#


if __name__ == '__main__':
    adj_dict = dict()
    graph_from = [1] * 10
    graph_to = list(range(20, 30))
    adj_dict = dict()
    for s, t in zip(graph_from, graph_to):
        adj_dict.setdefault(s - 1, set()).add(t - 1)

    ice_cream = defaultdict(int)
    ice_cream['Sarah'] = 23
    ice_cream['Abdul'] = 13


    # defaultdict( < type 'int' >, {'eggs': 1, 'spam': 7})
    i=7
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # graph_nodes, graph_edges = map(int, input().split())
    #
    # graph_from = [0] * graph_edges
    # graph_to = [0] * graph_edges
    #
    # for i in range(graph_edges):
    #     graph_from[i], graph_to[i] = map(int, input().split())
    #
    # ids = list(map(int, input().rstrip().split()))
    #
    # val = int(input())
    #
    # ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    #
    # fptr.write(str(ans) + '\n')
    #
    # fptr.close()
