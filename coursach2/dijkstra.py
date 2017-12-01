'''
Dijkstra algorithm implementation
'''
from collections import defaultdict

def generate_dijkstra_tree(nodes, root='root'):
    '''
    yield pair of neighbours
    '''
    def closest_node(weights, processed):
        '''
        return node with lowest weight
        '''
        closest_node = None
        for node in weights:
            if (weights[node] < weights.get(closest_node, float('inf'))
                    and node not in processed):
                closest_node = node
        return closest_node

    processed = set()
    weights = defaultdict(lambda: float('inf'), nodes[root])
    for node in weights:
        yield node, root

    while True:
        node = closest_node(weights, processed)
        if node is None:
            break
        neighbours = nodes[node]
        for neighbour in neighbours:
            new_weight = weights[node] + neighbours[neighbour]
            if new_weight < weights[neighbour]:
                weights[neighbour] = new_weight
                yield neighbour, node
        processed.add(node)
