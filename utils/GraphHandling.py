import pydot
from IPython.display import display, Image
from dataclasses import dataclass


@dataclass
class Color:
    green = "#008000"
    red = "#FF0000"


def sommets(G):
    S = set()
    for i in G:
        S.add(i)
        for j in G[i]:
            S.add(j)
    return sorted(S)


def arcs(G):
    arc = set()
    for i in G:
        for j in G[i]:
            arc.add(i + j)
    return sorted(arc)




def trace_G(G, genre, color):
    if genre == 0:
        graph = pydot.Dot(graph_type="graph")
    else:
        graph = pydot.Dot(graph_type="digraph")
    for i in G:
        node = pydot.Node(i)
        graph.add_node(node)
        for j in G[i]:
            arc = pydot.Edge(i, j, color=color)
            graph.add_edge(arc)
    return graph


# Function to combine two graphs
def combine_graphs(graph1, graph2):
    for node in graph2.get_nodes():
        graph1.add_node(node)

    for edge in graph2.get_edges():
        graph1.add_edge(edge)

    return graph1

def save_graph_as_image(graph, file_name: str):
    file_name = f"{file_name}.png"
    graph.write_png(file_name)
    img = Image(filename=file_name)
    display(img)


def minimize_edge_crossings(graph):
    graph.set_prog("neato")  # Neato is a Graphviz layout program that attempts to minimize edge crossings
    graph.set_overlap("scale")
    graph.set_splines("true")
