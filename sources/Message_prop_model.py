import random 
def message_prop(graph,seed_nodes,prob):
    active_nodes = set(seed_nodes)
    new_active_nodes = set(seed_nodes)

    while new_active_nodes:
        current_node = new_active_nodes.pop()
        neighbors = set(graph.neighbors(current_node)) - active_nodes

        for neighbor in neighbors:
            edge = (current_node,neighbor)
            if random.random() < prob.get(edge,0):
                new_active_nodes.add(neighbor)
                active_nodes.add(neighbor)
    return active_nodes