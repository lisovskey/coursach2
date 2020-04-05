'''
Generation helpers
'''
import math
from random import randint


def generate_dots(num, width, height):
    '''
    yield tuple of x, y coordinates
    '''
    for _ in range(num):
        yield randint(0, width), randint(0, height)

def generate_graph(dots, neighbourhood_size, distance_range=(10, 100)):
    '''
    yield tuple of id and node with distances to its neighbours
    '''
    def distance(node_id, neighbour_id):
        '''
        return random or existing distance
        '''
        if graph.get(neighbour_id):
            return graph[neighbour_id][node_id]
        return randint(*distance_range)

    graph = {}
    for node_id, _ in enumerate(reversed(dots)):
        node = {}
        for delta in range(1, neighbourhood_size + 1):
            neighbour_id = node_id + delta
            if neighbour_id < len(dots):
                node[neighbour_id] = distance(node_id, neighbour_id)
            neighbour_id = node_id - delta
            if neighbour_id >= 0:
                node[neighbour_id] = distance(node_id, neighbour_id)
        graph[node_id] = node
    return graph
