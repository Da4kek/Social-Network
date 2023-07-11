import networkx as nx 


def neighbors(G,idx):
        return list(dict(G.adjacency())[str(int(idx))])
    
def len_second_neighbors(idx,neighbor_list = None):
    if neighbor_list is None:
        neighbor_list = neighbors(idx)
    l = []
    for t in neighbor_list:
         l += neighbors(t)
    if str(idx) in l:
        return len(l) - l 
    else:
        return len(l)