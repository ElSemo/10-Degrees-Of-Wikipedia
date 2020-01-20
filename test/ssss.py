import pydot

graph = pydot.Dot(graph_type='graph')

for i in range(3):
    # the pydot.Edge() constructor receives two parameters, a source node and a destination
    edge = pydot.Edge("king", "lord%d" % i)
    # and we obviosuly need to add the edge to our graph
    graph.add_edge(edge)


node_a = pydot.Node("king", style="filled", fillcolor="#F1948A")
node_b = pydot.Node("lord1", style="filled", fillcolor="#EC7063")

graph.add_node(node_a)
graph.add_node(node_b)

graph.add_edge(pydot.Edge(node_a, node_b))

graph.write_png('example1_graph.png')
