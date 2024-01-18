import pandas as pd

from utils import *
from People import *


# List of summits
G = dict()
# Retrieve the type of graph
genre = 1  # input()


# Read CSV file into a DataFrame
csv_file_path = "inputData.csv"
df = pd.read_csv(csv_file_path, delimiter=';')


# Create Pupil instances from the DataFrame
pupils = create_pupils_from_dataframe(df)

print(pupils)

for pupil in pupils:
    a = pupil.name
    if a not in G:
        G[a] = []
    for like in pupil.likes:
        b = like
        G[a].append(b)
        sommets(G)
        arcs(G)
        like_graph = trace_G(G, genre, Color.green)

G.clear()
for pupil in pupils:
    a = pupil.name
    if a not in G:
        G[a] = []
    for dislike in pupil.dislikes:
        b = dislike
        G[a].append(b)
        sommets(G)
        arcs(G)
        dislike_graph = trace_G(G, genre, Color.red)

graph = combine_graphs(like_graph, dislike_graph)
minimize_edge_crossings(graph)
save_graph_as_image(graph, "Soziogramm")







