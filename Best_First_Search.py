from queue import PriorityQueue

def best_first_search(graph, heuristics, start, goal):
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    visited = []
    
    while not pq.empty():
        heuristic, node = pq.get()
        if node in visited:
            continue
        print(f"Visited node {node} with heuristic {heuristic}")
        visited.append(node)
        
        if node == goal:
            print("Goal node found")
            return
        
        for node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristics[neighbor], neighbor))
    print('goal node not found')
    
def input_graph():
    graph={}
    num = int(input("Enter the number of nodes: "))
    for i in range(num):
        node = input(f"Enter the node {i+1}: ")
        neighbors = input(f"Enter the neighbors of node {node}: ").split()
        graph[node]=neighbors
    return graph

def input_heuristics(graph):
    heuristics={}
    for node in graph:
        heuristic = int(input(f"Enter the heuristic value for node {node}: "))
        heuristics[node] = heuristic
    return heuristics

if __name__ == "__main__":
    graph = input_graph()
    heuristics = input_heuristics(graph)
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    print("Best First Search : \n")
    best_first_search(graph, heuristics, start,goal)
                
    