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
        return min(node for node in weights.items() if node not in processed, key=weights.get)

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
