from functools import reduce
import pandas as pd
import csv

def reg_create_csv(list_1, list_2):
    t_path = r'C:\Users\Eyal-TLV\Desktop\tmo_list.csv'
    with open(t_path, "w+") as f:
        f.write("".join(str(list_1)))
        f.write("\n")
        f.write("".join(str(list_2)))


def pnd_create_csv(list_1, list_2):
    t_path = r'C:\Users\Eyal-TLV\Desktop\pandas_list.csv'
    df_1 = pd.DataFrame(data=list_1,columns=['Actual'])
    df_2 = pd.DataFrame(data=list_2,columns=['Predicted'])
    df_3 = pd.DataFrame(data=list_2, columns=['Predicted2'])
    res_df = df_1.join(df_2).join(df_3)
    res_df[['Actual','Predicted','Predicted2']].to_csv(t_path, sep=',',index=True, index_label=["Index"])
    i = 6

def csv_create_csv(list_1, list_2):
    t_path = r'C:\Users\Eyal-TLV\Desktop\csv_list.csv'
    with open(t_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list_1)
        writer.writerow(list_2)

    # with open(t_path, "r") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         print(row['first_name'], row['last_name'])


if __name__ == '__main__':
    l_list = list(range(1,51))
    l_list_2 = list(range(1,100,2))
    # list(enumerate(l_list, 1))
    i = 5
    print("Yes") if i>6 else print("No")

    merge_list = list(zip(l_list,l_list_2))
    l1,l2 = list(zip(*merge_list))
    reduce(lambda x, y: x + y, filter(lambda x: x > 400, map(lambda i: i * i, l_list)))
    # reg_create_csv(l_list, l_list_2)
    pnd_create_csv(l_list, l_list_2)
    # csv_create_csv(l_list, l_list_2)
    i=6