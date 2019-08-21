from collections import defaultdict


def create_bars_dict(source_path):
    budgets = [10, 20, 30, 40, 50, 150]
    with open(source_path) as f:
        content = f.readlines()
    cont_dict = {'Oracle': [], 'Predicted': [], 'PathExistence': [], 'Random': []}
    for line in content:
        s_line = line.split(",")
        cont_dict[s_line[0]] = s_line[1:]

    res_dict = defaultdict(list)

    for budget in budgets:
        res_dict[str(budget)].append(len([i for i in cont_dict['Oracle'] if int(i) < budget]))
        res_dict[str(budget)].append(len([i for i in cont_dict['Predicted'] if int(i) < budget]))
        res_dict[str(budget)].append(len([i for i in cont_dict['PathExistence'] if int(i) < budget]))
        res_dict[str(budget)].append(len([i for i in cont_dict['Random'] if int(i) < budget]))

    return res_dict


def create_bars_file(file_path, res_dict):
    with open(file_path, "w") as f:
        f.write("budget,numOracle,numPredicted,numPathExistence,numRandom\n")
        for key in res_dict.keys():
            str_insert = str(key) + "," + ",".join([str(i) for i in res_dict[key]]) + "\n"
            f.write(str_insert)


if __name__ == '__main__':
    returned_dict = create_bars_dict(r'C:\Users\user\Desktop\graph_data\baseline\bars_plot_lang.csv')
    create_bars_file(r'C:\Users\user\Desktop\graph_data\baseline\bars_file_lang.csv', returned_dict)

