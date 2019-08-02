import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == "__main__":

    while True:
        rw = RandomWalk(50000)
        rw.fill_walk()
        plt.figure(figsize = (10,6), dpi = 128)
        point_numbers = list(range(rw.num_points) )
        plt.scatter(rw.x_values, rw.y_values, s=1,  c=point_numbers, cmap=plt.cm.Blues, edgecolor = 'none')
        #Emphisize first and last points
        plt.scatter(0, 0, s=100,  c='green')
        plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100,  c='red')

        # Remove axes
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)


        plt.show()


        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break