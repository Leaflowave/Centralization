import networkx as nx
import linecache
def CollegeMsgNetwork(init,end,network=None):
    if not network is None:
        nodes = set(network.nodes())
        edges=set(network.edges())
    else:
        nodes=set()
        edges=set()
    for i in range(init,end+1):
        temp= linecache.getline("dataEpoch//CollegeMsg.txt", i)
        temp=temp.split(" ")
        temp1=int(temp[0])
        temp2=int(temp[1])
        nodes.update([temp1,temp2])
        edges.update([(temp1,temp2)])
    G=nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G
