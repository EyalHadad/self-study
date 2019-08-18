import sys
import pygal
from pygal.style import Style
import matplotlib.pyplot as plt
import networkx as nx
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS,  LightenStyle as LS


def remove_postfix(my_string, list_chars):
    for char in list_chars:
        if char in my_string:
            my_string=my_string[:my_string.index(char)]
    return my_string

def create_my_graph(call_graph_path):
    f = open(call_graph_path)
    content = f.readlines()
    f.close()
    G = nx.DiGraph()
    for line in content:
        if line.startswith("M:"):
            e1 = line.split(" ")[0][2:]
            e2 = line.split(" ")[1]
            if e2[0:3] != "(I)":
                e2 = e2[3:]
                e1 = remove_postfix(e1, ['(', '$'])
                e2 = remove_postfix(e2, ['(', '$'])
                G.add_edge(e1, e2)
    return G


def get_trace(trace_path):
    with open(trace_path) as f:
        content = f.readlines()
    trace_dic = {}
    test_name = ''
    for line in content:
        if line.startswith("#test"):
            tmp_test_name = line[6:-1]
            k = tmp_test_name.rfind(".")
            test_name = tmp_test_name[:k] + ':' + tmp_test_name[k+1 : ]
        elif line.startswith("#trace"):
            func_str = line[7:-2]
            func_name_list = func_str.split("@")
            func_name_list_to_insert = []
            for name in func_name_list:
                tmp_name = name
                if '(' in name:
                    tmp_name = (name[:name.index('(')])

                k = tmp_name.rfind(".")
                name = tmp_name[:k] + ':' + tmp_name[k + 1:]
                func_name_list_to_insert.append(name)
            trace_dic[test_name] = func_name_list_to_insert

    return trace_dic


def trace_in_call_graph(graph_edges, trace_graph):
    counter = 0
    for e1, e2 in zip(trace_graph[:-1], trace_graph[1:]):
        if (e1,e2) in graph_edges:
            counter += 1
    return counter / (len(trace_graph) - 1)



def create_graph(call_graph_path, trace_path):
    G = create_my_graph(call_graph_path)
    trace_dic = get_trace(trace_path)
    results = []
    part_trace_in_cg, trace_cg_proportaion, trace_length = 0,0,0

    for key,value in trace_dic.items():
        trace_length = len(value)
        if key in list(G.nodes) and trace_length > 0:
            node_set = nx.descendants(G, key)
            node_set.add(key)
            H = G.subgraph(node_set)
            trace_graph = value
            trace_graph.insert(0,key)
            part_trace_in_cg = trace_in_call_graph(list(H.edges),trace_graph)
            trace_cg_proportaion = (trace_length-1) / len(list(H.edges))
            results.append([trace_length, part_trace_in_cg, trace_cg_proportaion])
        else:
            part_trace_in_cg, trace_cg_proportaion = float('nan'),float('nan')
    return results


def write_results(results_list, result_file_path):
    with open(result_file_path, "w+") as f:
        f.writelines("Trace length, % Trace in CG, Trace_len/CG_size\n")
        for element in results_list:
            value_to_write = str(element)[1:-1]
            f.writelines(value_to_write + "\n")


def read_file_to_list(file_path):
    trace_length, trace_percentage, trace_graph_ration = [], [], []
    with open(file_path) as f:
        head = f.readline()
        content = f.readlines()
    for line in content:
        values = line.split(",")
        trace_length.append(int(values[0]))
        trace_percentage.append(float(values[1]))
        trace_graph_ration.append(float(values[2].rstrip()))

    return trace_length, trace_percentage, trace_graph_ration


def create_length_bars(lists, file_name):
    frequencies,frequencies_percentage = [],[]
    for res_list in lists:
        for value in range(min(res_list), max(res_list)):
            frequency = res_list.count(value)
            frequencies.append(frequency)
    sum_count = sum(frequencies)
    for freq in frequencies:
        frequencies_percentage.append((freq/ sum_count) * 100)
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1500

    hist = pygal.Bar(my_config, style = my_style)

    hist.title = file_name.title() + " Trace length"

    # hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    hist.x_title = "Length"
    hist.y_title = "% of tests"
    # hist.value_formatter = lambda y: "%.0f%" % y
    # hist.x_value_formatter = lambda y: "$%.2f" % y

    hist.add('Length', frequencies_percentage)
    hist.x_labels = sorted(set(frequencies))
    hist.render_to_file(file_name.title() + '_trace_length.svg')

if __name__ == "__main__":
    results = create_graph('callGraph_lang_16.txt', 'traceFile_lang_16.txt')
    # write_results(results, 'traceDetails.csv')
    # trace_length, trace_percentage, trace_graph_ration = read_file_to_list('traceDetails_lang.csv')
    # create_length_bars([trace_length], 'lang')

    # trace_length, trace_percentage, trace_graph_ration = read_file_to_list('traceDetails_math.csv')
    # create_length_bars([trace_length], 'math')



