from algorithms.graph.traversal import dfs_traverse,bfs_traverse,dfs_traverse_recursive

graph = {'A': set(['B', 'C', 'F']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['A', 'C', 'E'])}

print(dfs_traverse(graph, 'A'))

print(bfs_traverse(graph, 'A'))

print(dfs_traverse_recursive(graph, 'A'))

def find_path(graph, start, end, visited=[]):

    visitied = visited + [start]
    if start == end:
        return visited
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in visited:
            new_visited = find_path(graph, node, end, visited)
            return new_visited
    return None


print(find_path(graph, 'A', 'F'))