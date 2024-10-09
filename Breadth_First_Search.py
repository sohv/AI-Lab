from collections import deque

# Function to implement BFS
def bfs(graph, start):
    visited = []  # List to keep track of visited nodes
    queue = deque([start])  # Queue initialized with the starting node
    
    while queue:
        node = queue.popleft()    
        # If the node has not been visited, mark it as visited
        if node not in visited:
            visited.append(node)
            print(f"Visited {node}")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        neighbors = input(f"Enter neighbors of {node}: ").split()
        graph[node] = neighbors
    
    return graph

if __name__ == "__main__":
    graph = input_graph()
    start_node = input("Enter the start node for BFS: ")
    print("\nBreadth-First Search traversal:")
    bfs(graph, start_node)
