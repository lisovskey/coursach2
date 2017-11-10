from random import randint

def generate_dots(num, width, height):
    '''
    yield tuple of x, y coordinates
    '''
    for _ in range(num):
        yield randint(0, width), randint(0, height)

def generate_graph(dots, neighboorhood_size, distance_range=(10, 100)):
    '''
    yield tuple of id and node with distances to its neighboors
    '''
    def distance(node_id, neighboor_id):
        '''
        return random or existing distance
        '''
        if graph.get(neighboor_id):
            return graph[neighboor_id][node_id]
        else:
            return randint(*distance_range)

    graph = {}
    for node_id, _ in enumerate(reversed(dots)):
        node = {}
        for delta in range(1, neighboorhood_size + 1):
            neighboor_id = node_id + delta
            if neighboor_id < len(dots):
                node[neighboor_id] = distance(node_id, neighboor_id)
            neighboor_id = node_id - delta
            if neighboor_id >= 0:
                node[neighboor_id] = distance(node_id, neighboor_id)
        graph[node_id] = node
    return graph
