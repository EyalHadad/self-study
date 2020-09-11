import matplotlib.pyplot as plt
from collections import Counter

path = r'C:\Users\Eyal-TLV\Desktop\Dataset\drugs_data\tables _to_upload\taxonomic_lineage.csv'
with open(path) as f:
    cont = f.readlines()[1:]
    x,y = zip(*sorted(Counter(map(lambda x: len(x.split(":")), cont)).items()))
    plt.title('Taxonomic Sequence Lengths', fontsize=20,weight="bold")
    plt.xlabel('Length', fontsize=18)
    plt.ylabel('#Number of proteins', fontsize=16)
    plt.xticks(range(1,len(x)+1),[str(i) for i in range(1,len(x)+1)] , rotation=90)
    bar1 = plt.bar(x,y,width=0.7)
    for rect in bar1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom')

    plt.show()


