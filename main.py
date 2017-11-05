from kruskal import Algoritimo_kruskal as kr
import networkx as nx
graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])

grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
grafo.add_edges_from([
                            ('A', 'B', {'weight': 1}), 
                            ('A', 'C', {'weight': 5}), 
                            ('A', 'D', {'weight': 3}),
                            ('B', 'C', {'weight': 4}),  
                            ('B', 'D', {'weight': 2}), 
                            ('C', 'D', {'weight': 1}), 
                            ])
arvore_minima = nx.Graph()
arvore_minima.add_nodes_from((['A', 'B', 'C', 'D']))
arvore_minima.add_edges_from([
                            ('A', 'B', {'weight': 1}), 
                            ('B', 'D', {'weight': 2}), 
                            ('C', 'D', {'weight': 1}),
                            ])

grafo2 = nx.Graph()
grafo2.add_weighted_edges_from([
                            (1,2,4),
                            (1,3,8),
                            (2,3,11),
                            (2,4,8),
                            (3,6,7),
                            (3,7,1),
                            (6,4,2),
                            (6,7,20),
                            (7,8,2),
                            (4,8,4),
                            (5,8,14),
                            (5,9,9),
                            (8,9,10),
                            (4,5,7)
                            ])


k = kr()
#assert kruskal(grafo) == arvore_minima
mst = k.kruskal(grafo2)
print(mst.edges)
print(k.peso(mst))