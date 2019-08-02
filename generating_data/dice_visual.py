from dice import Die
import pygal
from pygal.style import Style

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
for value in range(2,die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


blue = Style(colors=('green',))
hist = pygal.Bar(style = blue)
hist.title = "Results of rolling 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11', '12','13','14','15','16']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"


hist.add('D6 + D10',frequencies)
# hist.add('D6 + D6_copy',frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)