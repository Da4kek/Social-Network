import pandas as pd
import numpy as np 

def make_nodes(df):
    node_list = df.node1.unique()
    node_str = []
    for n in node_list:
        node_str.append(str(n))
    return node_str

def make_embedding(nodes,model_):
    embedding_df = pd.DataFrame()
    for node in nodes:
        transpose_single_node = pd.DataFrame(model_.wv.get_vector(node)).T 
        embedding_df = embedding_df.append(transpose_single_node)
        embedding_df = embedding_df.reset_index(drop=True)
    return embedding_df

