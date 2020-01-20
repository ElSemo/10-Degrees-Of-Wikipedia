import pydot
import Search as Se
import pymysql

# Initialize digraph
graph = pydot.Dot(graph_type='digraph')

# Connect to SQL
connection = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='5565', db='mysql', charset='utf8')
crs = connection.cursor()
crs.execute('USE wiki')

# Fetch link data
crs.execute('SELECT fromPageId, toPageId FROM links LIMIT 10')

# Construct directed graph
for link in crs.fetchall():
    fromPageId = Se.getUrl(link[0])[6:]
    toPageId = Se.getUrl(link[1])[6:]
    edge = pydot.Edge(fromPageId, toPageId)
    graph.add_edge(edge)

# Find a link
nodes = Se.getLinks(1)
targetPageId = 3000
pageIds = Se.BFS(targetPageId)

# Color the link of choice
node_a = pydot.Node(Se.getUrl(pageIds[0])[6:], style="filled", fillcolor="#F1948A")
node_b = pydot.Node(Se.getUrl(pageIds[1])[6:], style="filled", fillcolor="#EC7063")
node_c = pydot.Node(Se.getUrl(pageIds[2])[6:], style="filled", fillcolor="#E74C3C")
node_d = pydot.Node(Se.getUrl(pageIds[3])[6:], style="filled", fillcolor="#CB4335")
node_e = pydot.Node(Se.getUrl(pageIds[4])[6:], style="filled", fillcolor="#943126")
node_f = pydot.Node(Se.getUrl(pageIds[5])[6:], style="filled", fillcolor="#78281F")

graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)
graph.add_node(node_e)
graph.add_node(node_f)

graph.add_edge(pydot.Edge(node_a, node_b))
graph.add_edge(pydot.Edge(node_b, node_c))
graph.add_edge(pydot.Edge(node_c, node_d))
graph.add_edge(pydot.Edge(node_d, node_e))
graph.add_edge(pydot.Edge(node_e, node_f))

graph.write_png('DegreesOfWiki_graph.png')
