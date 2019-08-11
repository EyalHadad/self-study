import requests
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS,  LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
repo_dicts = r.json()['items']

names, plot_dicts = [], []
for repo in repo_dicts:
    names.append(repo['name'])
    description = repo['description']
    if not description:
        description = "No description provided."
    plot_dict = {
        'value':repo['stargazers_count'],
        'label':description,
        'xlink':repo['html_url']
    }
    plot_dicts.append(plot_dict)


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
chart = pygal.Bar(my_config, style = my_style)
# chart = pygal.Bar(my_config)
chart.title = 'Most-Starred Python projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
