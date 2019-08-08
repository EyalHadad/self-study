import json
from country_codes import get_country_code
from pygal_maps_world import maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

def run_world_code():
    filename = 'population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population

    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc, pop in cc_populations.items():
        if pop<10000000:
            cc_pops_1[cc] = pop
        elif pop<1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop



    # wm_style = RS('#336699', base_style=LCS)
    # wm = maps.World(style=wm_style)
    wm = maps.World()
    wm.title = 'World population'
    wm.add('0-10m', cc_pops_1)
    wm.add('10-1b', cc_pops_2)
    wm.add('>1b', cc_pops_3)
    wm.render_to_file('world_population.svg')




if __name__ == '__main__':
    run_world_code()
