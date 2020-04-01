import json
import pandas as pd


def read_file(path):
    rows = []
    title, ingrediant, link = [], [], []
    total_ingrediant = set()
    with open(path, mode='r', encoding="utf8") as ings:
        content = json.load(ings)

    for recipe in content:
        title.append(recipe['Title'])
        ingrediant.append('@'.join(set(recipe['Ing_Names'])))
        link.append(recipe['Link'])
        total_ingrediant.update(set(recipe['Ing_Names']))
    rows = zip(title, ingrediant, link)
    data = pd.DataFrame(rows, columns=['title', 'ingrediant', 'link'])
    pandas_args = pd.DataFrame(total_ingrediant)

    pandas_args.to_csv('list_args.csv', encoding='utf-8-sig')
    data.to_csv('recipes.csv', encoding='utf-8-sig')
    i = 6


def rank_recpie(existing_args):
    data = pd.read_csv("recipes.csv")
    rank_dict = {}
    for index, row in data.iterrows():
        recipe_ing = row['ingrediant'].split("@")
        rank_dict[str(index)] = len(set(recipe_ing).intersection(existing_args))


    i=6



if __name__ == '__main__':
    # input_path = r'C:\Users\Eyal_J\Desktop\quotes_spider\items.json'
    # read_file(input_path)
    rank_recpie(['קמח', 'חומץ'])
