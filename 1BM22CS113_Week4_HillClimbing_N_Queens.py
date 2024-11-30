
def calculate_heuristic(state):
    heuristic = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]: 
                heuristic += 1
            if abs(state[i] - state[j]) == abs(i - j):  
                heuristic += 1
    return heuristic
def generate_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]  
            neighbors.append(new_state)
    return neighbors
def print_board(state):
    n = len(state)
    board = [['.'] * n for _ in range(n)]
    for row in range(n):
        board[state[row]][row] = 'Q'
    for row in board:
        print(' '.join(row))
    print()
def hill_climbing_n_queens(initial_state):
    current_state = initial_state
    
    while True:
        current_heuristic = calculate_heuristic(current_state)
        print(f"Current State: {current_state}, Heuristic: {current_heuristic}")
        print_board(current_state)  
        
        if current_heuristic == 0:
            return current_state
        
        neighbors = generate_neighbors(current_state)
        best_neighbor = None
        best_heuristic = float('inf')
        
        for neighbor in neighbors:
            heuristic = calculate_heuristic(neighbor)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_neighbor = neighbor
        
        if best_heuristic >= current_heuristic:
            break  
        
        current_state = best_neighbor
    
    return None  
def solve_n_queens():
    n = int(input("Enter the number of queens: "))
    initial_state = []
    print(f"Enter the row positions of the queens for each column (0 to {n-1}):")
    for i in range(n):
        pos = int(input(f"Queen in column {i}: "))
        if pos < 0 or pos >= n:
            print(f"Invalid input. Please enter a number between 0 and {n-1}.")
            return
        initial_state.append(pos)
    solution = hill_climbing_n_queens(initial_state)
    if solution:
        print(f"Solution found for {n}-Queens problem: {solution}")
        print_board(solution)  # Print the final board
    else:
        print("No solution found.")
solve_n_queens()
