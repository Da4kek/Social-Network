def FitnessFunc(In_degree,Out_degree,Graph):
    Nodes_ = []
    Fitness_ = []
    for node in Graph.nodes():
        Nodes_.append(node)
        Fitness_.append(In_degree[node]/(In_degree[node] + Out_degree[node])**2)
    return Nodes_,Fitness_