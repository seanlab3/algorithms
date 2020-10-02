"""
Given a directed graph, check whether it contains a cycle.
Real-life scenario: deadlock detection in a system. Processes may be
represented by vertices, then and an edge A -> B could mean that process A is
waiting for B to release its lock on a resource.
"""
from algorithms.graph.cycle_detection  import TraversalState,contains_cycle

example_graph_with_cycle = {'A': ['B', 'C'],
                            'B': ['D'],
                            'C': ['F'],
                            'D': ['E', 'F'],
                            'E': ['B'],
                            'F': []}

example_graph_without_cycle = {'A': ['B', 'C'],
                               'B': ['D', 'E'],
                               'C': ['F'],
                               'D': ['E'],
                               'E': [],
                               'F': []}
print(contains_cycle(example_graph_with_cycle))
print(contains_cycle(example_graph_without_cycle))