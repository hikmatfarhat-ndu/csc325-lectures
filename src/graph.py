import networkx as nx 
#G=nx.Graph()
G=nx.erdos_renyi_graph(10000,0.2)
#l=nx.maximal_independent_set(G)
#l=(list(G.edges))
k=len(nx.maximal_independent_set(G))
print(inset)
#for u,v in G.edges:
#    print("edge from {} to {}".format(u,v))
