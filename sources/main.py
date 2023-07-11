import pandas as pd 
import numpy as np
import networkx as nx 
from sources.data_prep import make_nodes,make_embedding
from sklearn.metrics.pairwise import cosine_similarity
from node2vec import Node2Vec

df = pd.read_csv("facebook_combined.txt",sep=" ")

Graph = nx.from_pandas_edgelist(df,source="node1",target="node2")


edge_list = list(zip(df['node1'],df['node2']))

combined_graph = nx.Graph(edge_list)

n2v_obj = Node2Vec(combined_graph,dimensions=64,walk_length=5,num_walks=10,p=1,q=1,workers=1)
model = n2v_obj.fit(window=10,min_count=1,batch_words=4)

nodes = make_nodes(df)

embedding_df = make_embedding(nodes,model)

embedding_df.to_csv("embedding_data.csv")