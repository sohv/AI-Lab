# using priority queue through heapq
import heapq

# Function to implement Uniform Cost Search
def uniform_cost_search(graph, start, goal):
    # Priority queue (min-heap) to store (cost, node, path)
    pq = [(0, start, [])]  # (initial cost, start node, empty path)
    
    visited = set()  # To keep track of visited nodes

    while pq:
        # Pop the node with the smallest cost
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        # Add the current node to the path
        path = path + [node]
        # If we reached the goal, return the cost and the path
        if node == goal:
            return cost, path
        # Explore neighbors of the current node
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

    return float('inf'), []

def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))   
    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        neighbors = int(input(f"Enter the number of neighbors for {node}: "))
        graph[node] = []
        for j in range(neighbors):
            neighbor = input(f"Enter neighbor {j+1} of {node}: ")
            edge_cost = int(input(f"Enter the edge cost from {node} to {neighbor}: "))
            graph[node].append((neighbor, edge_cost))
    return graph

if __name__ == "__main__":
    graph = input_graph()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    cost, path = uniform_cost_search(graph, start_node, goal_node)
    if path:
        print(f"\nUniform Cost Search found a path: {path} with cost {cost}")
    else:
        print(f"\nNo path found from {start_node} to {goal_node}.")