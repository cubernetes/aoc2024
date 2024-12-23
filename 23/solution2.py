#!/usr/bin/env pypy3

import networkx as nx

G=nx.Graph()
for conn in open(0):
    a,b=conn.strip().split('-')
    G.add_edge(a, b)
print(','.join(sorted(list(nx.enumerate_all_cliques(G))[-1])))
