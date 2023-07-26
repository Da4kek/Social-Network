def FitnessFunc(In_degree,Out_degree,Graph):
    Nodes_ = []
    Fitness_ = []
    Edges_ = []
    for node in list(Graph.nodes()):
        Edges_.append(Graph.edges(node))
        Nodes_.append(node)
        Fitness_.append(In_degree[node]/(In_degree[node] + Out_degree[node])**2)
    return Nodes_,Fitness_,Edges_