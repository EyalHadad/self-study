import matplotlib.pyplot as plt


def create_scatters():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm.Blues)
    # Set chart title and label axes
    plt.title("Square Numbers", fontsize=18)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=12)
    # Set size of tick labels
    plt.tick_params(axis='both', labelsize=10, which='major')
    # Set the range for each axes
    plt.axis([0, 1100, 0, 1100000])
    # plt.figure(num = "Figure 1", figsize=(5,5))
    # plt.rcParams['figure.figsize'] = (400,160)
    plt.savefig('my_plot_tight.png', bbox_inches='tight')
    # plt.savefig('my_plot_tight.png' , bbox_inches =)
    plt.savefig('my_plot_reg.png')
    plt.show()

def plot_from_lists():
    squares = [1, 4, 9, 16, 25]
    input_values = list(range(1, 6))
    plt.plot(input_values, squares, linewidth=5)
    # Set chart title and label axes
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # Set size of tick labels
    plt.tick_params(axis='both', labelsize=14, color='red')
    plt.show()

# plot_from_lists()
create_scatters()
