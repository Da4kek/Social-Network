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

def message_prop_T(graph,seed_nodes,threshold):
    activated_nodes = seed_nodes
    new_activated_nodes = seed_nodes

    while new_activated_nodes:
        new_activated_nodes = []

        for node in activated_nodes:
            neighbors = list(graph.neighbors(node))

            for neighbor in neighbors:
                if (
                    graph.nodes[node].get('fitness',0) >= 0.2
                    and neighbor not in activated_nodes
                    and neighbor not in new_activated_nodes
                ):
                    new_activated_nodes.append(neighbor)

        activated_nodes.extend(new_activated_nodes)
    return activated_nodes