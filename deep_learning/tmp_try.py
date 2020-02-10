import numpy as np
my = [i for i in range(1000)]
big_array = np.zeros((3, 10))
input_lists = [[3, 6, 1], [1, 4, 7]]
for index, values in enumerate(input_lists):
    big_array[index, values] = 1

i = 6
