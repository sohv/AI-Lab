from collections import deque
def print_path(came_from, state):
    path = []
    while state:
        path.append(state)
        state = came_from.get(state)
    for step in reversed(path):
        print(step)

def water_jug_problem(capacity_a, capacity_b, goal):
    initial_state = (0, 0)  # (amount in jug A, amount in jug B)
    queue = deque([initial_state])
    came_from = {initial_state: None}    
    while queue:
        current_state = queue.popleft()
        a, b = current_state
        if a == goal or b == goal:
            print("Goal reached!")
            print_path(came_from, current_state)
            return
        possible_states = [
            (capacity_a, b),    # Fill jug A
            (a, capacity_b),    # Fill jug B
            (0, b),             # Empty jug A
            (a, 0),             # Empty jug B
            (max(0, a - (capacity_b - b)), min(capacity_b, b + a)),  # Pour A to B
            (min(capacity_a, a + b), max(0, b - (capacity_a - a)))   # Pour B to A
        ]
        for state in possible_states:
            if state not in came_from:
                came_from[state] = current_state
                queue.append(state)
    print("No solution found.")

if __name__ == '__main__':
    capacity_a = int(input("Enter the capacity of jug A: "))
    capacity_b = int(input("Enter the capacity of jug B: "))
    goal = int(input("Enter the goal amount of water: "))
    water_jug_problem(capacity_a, capacity_b, goal)
