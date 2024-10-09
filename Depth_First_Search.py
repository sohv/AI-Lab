# Function to implement DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []  # List to keep track of visited nodes
    if node not in visited:
        visited.append(node)  # Mark the current node as visited
        print(f"Visited {node}")
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
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
    # Input the graph from the user
    graph = input_graph()
    start_node = input("Enter the start node for DFS: ")
    print("\nDepth-First Search traversal:")
    dfs(graph, start_node)