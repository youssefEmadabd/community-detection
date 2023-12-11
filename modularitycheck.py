from modularity_maximization.utils import get_modularity
import networkx as nx
import numpy as np
import pandas as pd
import snap
gyoutube = nx.Graph(nx.read_gml("youtube/youtubegraph.gml"))

youtube = snap.TIntV()
for nodeId in range(5000):
    youtube.Add(nodeId)
print("modularity for Youtube graph:"+str(snap.GetModularity(gyoutube, youtube, 45968)))
