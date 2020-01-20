# -*- coding: utf-8 -*-
"""
pydot example 1
@author: Federico Cáceres
@url: http://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot
"""
import pydot # import pydot or you're not going to get anywhere my friend :D

# first you create a new graph, you do that with pydot.Dot()
graph = pydot.Dot(graph_type='graph')

# the idea here is not to cover how to represent the hierarchical data
# but rather how to graph it, so I'm not going to work on some fancy
# recursive function to traverse a multidimensional array...
# I'm going to hardcode stuff... sorry if that offends you

# let's add the relationship between the king and vassals
for i in range(3):
    # we can get right into action by "drawing" edges between the nodes in our graph
    # we do not need to CREATE nodes, but if you want to give them some custom style
    # then I would recomend you to do so... let's cover that later
    # the pydot.Edge() constructor receives two parameters, a source node and a destination
    # node, they are just strings like you can see
    edge = pydot.Edge("king", "lord%d" % i)
    # and we obviosuly need to add the edge to our graph
    graph.add_edge(edge)


node_a = pydot.Node("king", style="filled", fillcolor="#F1948A")
node_b = pydot.Node("lord1", style="filled", fillcolor="#EC7063")

graph.add_node(node_a)
graph.add_node(node_b)

graph.add_edge(pydot.Edge(node_a, node_b))

graph.write_png('example1_graph.png')