import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
V = ['joe', 'bob', 'ana', 'sam']
E = [('joe','ana', 5),('joe','sam', 4),('joe','bob', 1),('bob','sam', 3),('ana','sam',2)]
G.add_nodes_from(V)
G.add_weighted_edges_from(E)

pos = nx.shell_layout(G)

#FINDING THE SMALLEST EDGE FROM A NODE (weight only)
def SmallestEdge(G, v):
    edge = G.edges(v, data="weight")
    try:
        SmallestEdge = list(edge)[0]
    except:
        return "This graph has no edges"
    num = len(list(edge))
    for i in list(edge):
        if SmallestEdge[2] > i[2]:
            SmallestEdgeR = i
            if i == list(edge)[num-1]:
                return SmallestEdgeR
        else:
             if i == list(edge)[num-1]:
                SmallestEdgeR = i
                return SmallestEdgeR
      
            
#Prim's algorithm:
def PrimsMST(G,V,E):
    T = nx.Graph()
    T.add_node(V[0])
    MSTcost = 0
    
    i = -1
    edge = []
    
    while T.nodes() != G.nodes():
      edge.append(SmallestEdge(G, V[i+1])) #adds the smallest edge of a node to graph T
      if list(edge)[0][1] not in T.nodes(): #this checks if the nodes connected to the edges arent in T, if not it proceeds
         T.add_weighted_edges_from(edge)
      edge = []
      i = i+1
    return T
PrimsMST(G, V, E)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels, label_pos=0.3)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()

T = PrimsMST(G, V, E)
pos = nx.shell_layout(T)

edge_labels = nx.get_edge_attributes(T, "weight")
nx.draw_networkx_edge_labels(T, pos, edge_labels, label_pos=0.3)
nx.draw_networkx_nodes(T, pos)
nx.draw_networkx_labels(T, pos)
nx.draw_networkx_edges(T, pos)
plt.show()

total_weight = 0
for u, v, data in T.edges(data=True):
    total_weight = total_weight + data['weight']

print("If we were to assume a weight of 1 on a edge is 1 minute, then the rate at which the rumour spreads is " + str(total_weight) + " minutes")