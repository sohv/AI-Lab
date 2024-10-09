def valid(state):
    if state[0][0] < state[0][1] and state[0][0] > 0:
        return False
    if state[1][0] < state[1][1] and state[1][0] > 0:
        return False
    return True

def successors(state, total_m, total_c):
    children = []
    for i in range(total_m + 1):
        for j in range(total_c + 1):
            if i + j < 1 or i + j > 2:
                continue
            if state[2] == 1:  # boat on the left side
                child = ((state[0][0] - i, state[0][1] - j), (state[1][0] + i, state[1][1] + j), 0)
            else:  # boat on the right side
                child = ((state[0][0] + i, state[0][1] + j), (state[1][0] - i, state[1][1] - j), 1)
            
            if valid(child):
                children.append(child)
    return children

def bfs(start, goal, total_m, total_c):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for child in successors(node, total_m, total_c):
            if child not in visited:
                visited.add(child)
                new_path = list(path)
                new_path.append(child)
                queue.append(new_path)
    return []

def main_with_input():
    missionaries = int(input("Enter the number of missionaries: "))
    cannibals = int(input("Enter the number of cannibals: "))
    initial = ((missionaries, cannibals), (0, 0), 1)  
    goal = ((0, 0), (missionaries, cannibals), 0)    
    path = bfs(initial, goal, missionaries, cannibals)    
    if path:
        print("Solution found! Path:")
        for state in path:
            print(state)
    else:
        print("No solution found.")
if __name__ == "__main__":
    main_with_input()
