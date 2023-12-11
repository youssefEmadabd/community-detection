import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
from sklearn.manifold import TSNE
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
from sklearn.metrics.cluster import normalized_mutual_info_score
from modularity_maximization.utils import get_modularity
data = pd.read_csv('graphYB.csv')
data = np.array(data)
#labels = pd.read_csv('graphYB.csv')
print(data.size)
graph = nx.Graph()
for x in data:
 graph.add_edge(x[0],x[1])
node2vec = Node2Vec(graph, dimensions=16, walk_length=4, num_walks=4, workers=4)

model = node2vec.fit(window=10, min_count=1)

nodes = [x for x in model.wv.vocab ]
embeddings = np.array([model.wv[x] for x in nodes])
embeddings

tsne = TSNE(n_components=2, random_state=7, perplexity=15)
embeddings_2d = tsne.fit_transform(embeddings)
embeddings_2d

figure = plt.figure(figsize=(11, 9))

ax = figure.add_subplot(111)

ax.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c="black")
plt.show()
dendrogram = sch.dendrogram(sch.linkage(embeddings, method='ward'))

hc = AgglomerativeClustering(n_clusters=2150, affinity = 'euclidean', linkage='ward')#8,385

y_hc = hc.fit_predict(embeddings)
for x in y_hc:
  print(x)

print(len(y_hc))
#print(len(labels))
#labels = np.array(labels)
#true = []
pred = []
#for x in labels:
#  true.append(x[0])
for x in y_hc:
  pred.append(x)
print(pred)
#print(true)
outdata = {'communities':pred}
df = pd.DataFrame(outdata, columns = ['communities'])
df.to_csv('predictedbig.csv')

Com = {'communities':pred}
df = pd.DataFrame(Com, columns = ['communities'])
df.to_csv('lifejournal/outputCom2d.csv')
