from matplotlib import pyplot as plt

def show_plot(dots, graph=None, tree=None, path=None, size=(8, 8)):
    '''
    draw plot of dots with ids and lines with weights
    '''
    plt.figure(figsize=size)
    if path:
        for node_id, neighboor_id in path.items():
            plt.plot(*zip(dots[neighboor_id], dots[node_id]), 'g-', linewidth=3)
    if tree:
        for node_id, neighboor_id in tree.items():
            plt.plot(*zip(dots[neighboor_id], dots[node_id]), 'b-', linewidth=1.5)
    if graph:
        for node_id, node in graph.items():
            for neighboor_id, _ in node.items():
                plt.plot(*zip(dots[neighboor_id], dots[node_id]), 'k-', linewidth=0.2)
                plt.annotate(node[neighboor_id], color='tab:gray',
                             xy=((dots[node_id][0] + dots[neighboor_id][0]) / 2,
                                 (dots[node_id][1] + dots[neighboor_id][1]) / 2))
    if dots:
        for i, dot in enumerate(dots):
            plt.plot(*dot, marker='o', color='r', ls='')
            plt.annotate(i, color='r', xy=(dot[0] + 6, dot[1] - 4))
    plt.show()
