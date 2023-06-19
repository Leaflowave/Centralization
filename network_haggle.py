#coding=utf-8

"""
本程序对数据集做处理：
dataset=open("InternetTopology_Data.txt",'r')

"""
import ALG_Metrics
import networkx as nx
import linecache
def election_Data(init,end,network=None):
    if not network is None:
        G=network
        nodes=set(network.nodes())
        edges=set(network.edges())
    else:
        G = nx.Graph()
        nodes=set()
        edges=set()
    for i in range(init,end+1):
        temp=linecache.getline("dataEpoch//election_Data.txt", i)
        edge=eval(temp)
        edges.update(edge)
    # print len(edges)
    G.add_edges_from(edges)
    return G
def infectious(init,end,network=None):
    if not network is None:
        G=network
        nodes=set(network.nodes())
        edges=set(network.edges())
    else:
        G = nx.Graph()
        nodes=set()
        edges=set()
    for i in range(init,end+1):
        temp=linecache.getline("dataEpoch//infectious_data.txt", i)
        edge=eval(temp)
        edges.update(edge)
    # print len(edges)
    G.add_edges_from(edges)
    return G
# if __name__ == '__main__':
    # for i in range(100,1400,200):
    # for i in range(2000, 98000, 2000):
    #     G=election_Data(1,i)
    #     print nx.number_of_nodes(G)
    # G=email_Eu_core_Data(1,15000)
    # calculate_param.draw(G)