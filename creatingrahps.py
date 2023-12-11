import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
data = pd.read_csv('youtube/data.csv')
data = np.array(data)
data1 = pd.read_csv('lifejournal/data.csv')
data1 = np.array(data)
data2 = pd.read_csv('orkut/data.csv')
data2 = np.array(data)
graph = nx.Graph()
graph1 = nx.Graph()
graph2 = nx.Graph()
for x in range(24):
    z = (x * random.randint(2, 10))
    graph.add_edge(str(data[z][0]),str(data[z][1]))
    graph1.add_edge(str(data1[z][0]),str(data1[z][1]))
    graph2.add_edge(str(data2[z][0]),str(data2[z][1]))
nx.draw(graph, node_color=range(24), node_size=800, cmap=plt.cm.Reds)
plt.savefig('youtube/graphYT.png')
nx.write_gml(graph,"youtube/youtubegraph.gml")
nx.draw(graph1, node_color=range(24), node_size=800, cmap=plt.cm.Blues)
plt.savefig('lifejournal/graphLJ.png')
nx.write_gml(graph1,"lifejournal/lifejournalgraph.gml")
nx.draw(graph2, node_color=range(24), node_size=800, cmap=plt.cm.Reds)
plt.savefig('orkut/graphorkut.png')
nx.write_gml(graph2,"orkut/orkutgraph.gml")
