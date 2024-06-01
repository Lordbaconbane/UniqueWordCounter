'''Creates the bar graph from the unique_word_count'''
import matplotlib.pyplot as plt

def addlabels(x,y):
    '''Adds the labels to our graph'''
    for i in range(len(x)):
	    plt.text(i, y[i], y[i], ha = 'center')

def create_bar_graph(word_dict, max_x_axis):
    '''Creates the bar graph from the unique_word_count'''
    i = 0
    x_axis = []
    y_axis = []

    for key, value in word_dict.items():
        x_axis.append(key)
        y_axis.append(value)
        i+=1
        if i >= max_x_axis:
            break

    ax = plt.subplot()
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:purple', 'tab:olive', 'tab:cyan']
    ax.bar(x_axis, y_axis, color=bar_colors)
    ax.set_ylabel('# of counts')
    ax.set_title('Unique word count graph')
    addlabels(x_axis, y_axis)
    plt.show()
    return 0
