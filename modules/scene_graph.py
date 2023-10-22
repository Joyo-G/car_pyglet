"""
This module implements Scene Graphs using NetworkX
"""

from typing import Mapping
import networkx as nt
import numpy as np
import transforms as tr

__autor__ = "Gustavo Joyo"
__license__ = "MIT"
__version__ = "1.0.0"

class SceneGraph(nt.DiGraph):
    """
     Scene Graph
    """
    def __init__(self,incoming_graph_data = None,**args):
        super().__init__(incoming_graph_data,**args)
        super().add_node("root")
    """
    Add a graph to root node
    """
    def add_graph(self,graph,root="root",transform=tr.indentidy()):
        self.add_node(graph)
        self.add_edge(root,graph,transform)

    """
    Add node and its attributes
    """
    def add_node(self,node,root="root",
                           mesh=None,
                           position = np.array([0,0,0]), 
                           rotation = np.array([0,0,0]),
                           scale = np.array([0,0,0]),
                           transform=tr.indentidy()):
        super().add_node(node,mesh=mesh,
                              position = position,
                              rotation = rotation,
                              scale = scale)
        super().add_edge(root,node, transform = transform)

    """
    Replace use of graph.nodes[node] for get attributes of node using only graph[node]
    """
    def __getitem__(self, node):
        if node not in self.nodes:
            raise KeyError(f"{node} not in graph")
        return self.nodes[node]
