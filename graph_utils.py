#!/usr/bin/env python
"""Provides utils for file IO (file_to_edges) and making the graph (make_graph)

file_to_edges converts a text file containing edges and edge costs into an edge set
make_graph turns the edge set into a defaultdict, the standardized version of the graph used in all parts
"""

import errors

from collections import defaultdict

def make_graph(edges):
    '''
    turns list of tuples (edges) into defaultdict graph object

    '''
    graph = defaultdict(list)

    # for source, dest, cost in edges
    for v1, v2, cost in edges:
    	try:
    		if int(cost) != float(cost) or int(cost) < 0: raise ValueError
        	cost = int(cost)
    	except ValueError:
    		raise errors.BadEdgeCostError("The edge cost must be an integer, greater than or equal to 0")
        graph[v1].append((v2, cost))

    return graph

def file_to_edgeset(file_path):
    '''
    turns file with lines:
    AB5
    BC4
    CD8
    DC8
    DE6
    AD5
    CE2
    EB3
    AE7

    into list of tuples:
    [
        ("A", "B", 5),
        ("B", "C", 4),
        ("C", "D", 8),
        ("D", "C", 8),
        ("D", "E", 6),
        ("A", "D", 5),
        ("C", "E", 2),
        ("E", "B", 3),
        ("A", "E", 7),
    ]
    '''
    with open(file_path,'r') as f:
        edges = f.read().splitlines()
    
    edge_set = []
    for e in range(len(edges)):
        edge = edges[e]
        if len(edge) < 3:
            raise errors.BadFileContentsError('Failed to interpret line {0}, format must be [a-z|A-Z][a-z|A-Z][0-9]*'.format(e))
        if not edge[0].isalpha():
            raise errors.BadFileContentsError('The first letter ({0}) of line {1} isn\'t a character between A and Z'.format(e, edge[0]))
        if not edge[1].isalpha():
            raise errors.BadFileContentsError('The second letter ({0}) of line {1} isn\'t a character between A and Z'.format(e, edge[1]))
        if edge[0] == edge[1]:
            raise errors.BadFileContentsError('The first letter cannot be the same as the second letter (found on line {0})'.format(e))
        try:
            if float(edge[2:]) != int(edge[2:]) or int(edge[2:]) < 0: raise ValueError
            weight = int(edge[2:])
        except ValueError:
            raise errors.BadFileContentsError('The edge weight ({0}) of line {1} must be an integer, greater than or equal to 0'.format(e, edge[2:]))

        if (edge[0], edge[1]) in [(v1, v2) for (v1, v2, _) in edge_set]:
            raise errors.BadFileContentsError('An edge with v1 {0} and v2 {1} already exists in the edge set (found on line {2})'.format(edge[0], edge[1], e)) 

        new_edge = (edge[0], edge[1], weight)

        edge_set.append(new_edge)

    return edge_set