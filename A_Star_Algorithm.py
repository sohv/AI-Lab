from queue import PriorityQueue

def a_star_search(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    
    g_costs = {start: 0}
    while not pq.empty():
        f, current_node, path = pq.get()
        
        if current_node == goal:
            return path, g_costs[goal]
        
        for neighbor, cost in graph[current_node]:
            g = g_costs[current_node] + cost         
            if neighbor not in g_costs or g < g_costs[neighbor]:
                g_costs[neighbor] = g
                f = g + h(neighbor, goal)
                pq.put((f, neighbor, path + [neighbor]))  
                
    return None, float('inf')

def heuristic(node, goal):
    heuristic_values = {
        1: 3,
        2: 2,
        3: 1,
        4: 0
    }
    return heuristic_values[node]

def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))    
    for i in range(num_nodes):
        node = int(input(f"Enter node {i+1}: "))
        neighbors = int(input(f"Enter the number of neighbors for {node}: "))
        graph[node] = []
        for j in range(neighbors):
            neighbor = int(input(f"Enter neighbor {j+1} of {node}: "))
            cost = int(input(f"Enter the cost from {node} to {neighbor}: "))
            graph[node].append((neighbor, cost))   
    return graph

if __name__ == "__main__":
    graph = input_graph()    
    start_node = int(input("Enter the start node: "))
    goal_node = int(input("Enter the goal node: "))

    path, cost = a_star_search(graph, start_node, goal_node, heuristic)

    if path:
        print(f"\nA* Search found a path: {path} with cost {cost}")
    else:
        print(f"\nNo path found from {start_node} to {goal_node}.")