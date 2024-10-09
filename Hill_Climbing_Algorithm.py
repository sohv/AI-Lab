# perform hill climbing to find the most optimized path between start and end points
import random

def hill_climbing_search(f, neighbor_fn, start, max_iter=1000):
    current = start  # Start from the given initial point
    current_value = f(current)  # Evaluate the initial function value
    
    for _ in range(max_iter):
        # Generate neighbors of the current point
        neighbors = neighbor_fn(current)        
        # Find the best neighbor
        next_neighbor = max(neighbors, key=lambda x: f(x))
        next_value = f(next_neighbor)        
        if next_value <= current_value:
            break        
        # Move to the best neighbor
        current = next_neighbor
        current_value = next_value  
    return current, current_value
def user_defined_function(x):
    return -x**2 + 10*x  # Example quadratic function

# Function to generate neighboring solutions
def neighbor_function(x, step_size):
    return [x + dx for dx in [-step_size, 0, step_size]]  # Neighbors at the defined step size

if __name__ == "__main__":
    step_size = float(input("Enter the step size for neighbor generation: "))
    start_point = float(input("Enter the starting point (x) for the search: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))    
    '''x_min = 0
    x_max = 10   
    if start_point < x_min or start_point > x_max:
        print(f"Starting point must be between {x_min} and {x_max}.")
    else:
        # Perform Hill Climbing Search'''
    best_solution, best_value = hill_climbing_search(
            user_defined_function,
            lambda x: neighbor_function(x, step_size),
            start_point,
            max_iter=max_iterations
        )        
    print("Best solution: x =", best_solution, "Best value: f(x) =", best_value)