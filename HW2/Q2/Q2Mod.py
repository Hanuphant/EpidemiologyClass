#!/home/shrey/miniconda3/envs/cse8803e/bin/python

# Imports
import networkx as nx
from collections import Counter

def aggregate(G, rho):
    # Create a new network graph
    H = nx.Graph()
    # Get nodelist and edgelist of all networks
    # nodelist = set(node for g in G for node in g.nodes())
    edgelist = [edge for g in G for edge in g.edges()]
    edgedict = Counter(edgelist)
    for key in edgedict.keys():
        if edgedict[key] >= rho:
            H.add_edge(*key)
    return H

def main():
    return None

if __name__ == '__main__':
    main()