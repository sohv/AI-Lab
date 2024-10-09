import heapq

# A* Search Algorithm
def a_star_search(graph, start, goal, h):
    pq = []
    heapq.heappush(pq, (0, start, [start]))  # (f = g + h, node, path)

    # Dictionary to keep track of visited nodes and their costs
    g_costs = {start: 0}
    while pq:
        f, current_node, path = heapq.heappop(pq)
        if current_node == goal:
            return path, g_costs[goal]
        
        # Explore neighbors of the current node
        for neighbor, cost in graph[current_node]:
            g = g_costs[current_node] + cost         
            if neighbor not in g_costs or g < g_costs[neighbor]:
                g_costs[neighbor] = g  # Update the cost to reach the neighbor
                f = g + h(neighbor, goal)  
                heapq.heappush(pq, (f, neighbor, path + [neighbor]))  
                
    return None, float('inf')

# Predefined heuristic function
def heuristic(node, goal):
    # Example heuristic values for each node
    heuristic_values = {
        'a': 3,
        'b': 2,
        'c': 1,
        'd': 0  # Goal node
    }
    return heuristic_values[node]

# Function to input graph from user
def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))    
    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        neighbors = int(input(f"Enter the number of neighbors for {node}: "))
        graph[node] = []
        for j in range(neighbors):
            neighbor = input(f"Enter neighbor {j+1} of {node}: ")
            cost = int(input(f"Enter the cost from {node} to {neighbor}: "))
            graph[node].append((neighbor, cost))   
    return graph

if __name__ == "__main__":
    # Get graph input from user
    graph = input_graph()    

    # Get start and goal nodes from user
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    # Run A* Search algorithm
    path, cost = a_star_search(graph, start_node, goal_node, heuristic)

    # Output the result
    if path:
        print(f"\nA* Search found a path: {path} with cost {cost}")
    else:
        print(f"\nNo path found from {start_node} to {goal_node}.")