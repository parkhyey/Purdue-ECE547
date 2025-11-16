# Purdue ECE54700, HW5-6, Hye Yeon Park

import sys

print("HW5-6, Dijkstra's algorithm\n")

def dijkstra(graph, source, node_numbers):
    """
    Dijkstra's algorithm to find shortest paths from a source node to all other nodes in an undirected graph.
    """
    n = len(graph)
    
    # Initialize
    distances = [None] * n  # distances: shortest distances from source to all nodes
    distances[source] = 0
    N = set()  # Set of nodes with final distances
    previous = [-1] * n  # previous: previous nodes in shortest paths
    
    # Remaining nodes not included in N
    remaining = set(range(n))

    print(f"Dijkstra's Algorithm from node {node_numbers[source]}:")
    print(f"{'Step':<6} {'N':<40} " + " ".join([f"D({node_numbers[i]})" for i in range(n)]))
    print("-" * (80 + 6*n))
    
    # Initial state
    n_set_str = "{" + str(node_numbers[source]) + "}"
    dist_str = " ".join([f"{d:6d}" if d is not None else "  ∞   " for d in distances])
    print(f"{'Initial':<6} {n_set_str:<40} {dist_str}")
    
    iteration = 0

    # Find node w not in N with minimum distance
    while remaining:        
        min_dist = None
        w = None
        for node in remaining:
            if distances[node] is not None:
                if min_dist is None or distances[node] < min_dist:
                    min_dist = distances[node]
                    w = node     
        if w is None: # No more reachable nodes            
            break
        
        N.add(w)
        remaining.remove(w)
        iteration += 1
        
        # Update distances for all v not in N
        for v in remaining:
            if graph[w][v] is not None:
                new_dist = distances[w] + graph[w][v]
                if distances[v] is None or new_dist < distances[v]:
                    distances[v] = new_dist
                    previous[v] = w
        
        # Print current state
        n_set_str = "{" + ",".join([str(node_numbers[i]) for i in sorted(N)]) + "}"
        dist_str = " ".join([f"{d:6d}" if d is not None else "  ∞   " for d in distances])
        print(f"{iteration:<6} {n_set_str:<40} {dist_str}")
    
    return distances, previous

# Problem 2(a) Verification
print("Problem 2(a) Verification\n")

n_nodes = 11
graph = [[None] * n_nodes for _ in range(n_nodes)]

# Set distance to self = 0
for i in range(n_nodes):
    graph[i][i] = 0

# Node numbers for printing (1-indexed)
node_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Format: (node_i, node_j, weight)
# Using 0-indexed: 0=1, 1=2, 2=3, 3=4, 4=5, 5=6, 6=7, 7=8, 8=9, 9=10, 10=11
edges = [
    (0, 1, 1),   # Rome-Geneva (1-2)    
    (0, 2, 1),   # Rome-Paris (1-3)
    (0, 3, 1),   # Rome-Zanzibar (1-4)
    (0, 4, 3),   # Rome-Calcutta (1-5)
    (0, 5, 3),   # Rome-Tokyo (1-6)
    (1, 2, 1),   # Geneva-Paris (2-3)
    (1, 5, 3),   # Geneva-Tokyo (2-6)
    (1, 8, 3),   # Geneva-London (2-9)
    (2, 8, 2),   # Paris-London (3-9)
    (2, 10, 3),  # Paris-Rio de Janeiro (3-11)
    (3, 4, 1),   # Zanzibar-Calcutta (4-5)
    (3, 10, 2),  # Zanzibar-Rio de Janeiro (4-11)
    (4, 6, 3),   # Calcutta-Hong Kong (5-7)
    (4, 7, 1),   # Calcutta-Sydney (5-8)
    (5, 6, 1),   # Tokyo-Hong Kong (6-7)
    (6, 7, 2),   # Hong Kong-Sydney (7-8)
    (8, 9, 1),   # London-New York (9-10)
    (9, 10, 2),  # New York-Rio de Janeiro (10-11)
]

# Make undirected graph
for u, v, w in edges:
    graph[u][v] = w
    graph[v][u] = w

distances, previous = dijkstra(graph, 0, node_numbers)
print_paths(distances, previous, 0, node_numbers)

def print_paths(distances, previous, source, node_numbers):
    """Print shortest paths from source to all nodes, using 1-indexed node numbers."""
    print("\nShortest Paths from Node " + str(node_numbers[source]) + ":")
    print("-" * 80)
    for i, dist in enumerate(distances):
        if i == source:
            continue
        if dist is None:
            print(f"Node {node_numbers[source]} to Node {node_numbers[i]}: No path exists")
        else:
            path = []
            current = i
            while current != -1:
                path.append(str(node_numbers[current]))
                current = previous[current]
            path.reverse()
            print(f"Node {node_numbers[source]} to Node {node_numbers[i]}: {' → '.join(path):40s} (cost = {dist})")
