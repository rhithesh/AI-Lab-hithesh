# Moves: Up, Down, Left, Right
moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Convert puzzle to string format for hashing
def puzzle_to_string(puzzle):
    return ''.join(str(num) for row in puzzle for num in row)

# Print puzzle for better visualization
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

# DFS algorithm with recursion
def dfs_8_puzzle(current, goal, visited, path, depth=0, max_depth=20):
    if depth > max_depth:
        return False  # Limit depth to avoid infinite recursion
   
    visited.add(puzzle_to_string(current))
   
    if current == goal:
        return path  # Return the sequence of moves that solves the puzzle
   
    zero_pos = [(i, j) for i in range(3) for j in range(3) if current[i][j] == 0][0]
   
    for move, (dx, dy) in moves.items():
        x, y = zero_pos[0] + dx, zero_pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row[:] for row in current]
            new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][zero_pos[1]]

            if puzzle_to_string(new_state) not in visited:
                result = dfs_8_puzzle(new_state, goal, visited, path + [move], depth + 1, max_depth)
                if result:  # If solution found, propagate it up the recursion chain
                    return result
   
    return False  # If no solution found

# Function to get input from user
def get_input():
    start_state = []
    goal_state = []
   
    print("Enter the start state (3x3 matrix, row by row, with 0 representing the blank space):")
    for i in range(3):
        row = list(map(int, input().split()))
        start_state.append(row)
   
    print("Enter the goal state (3x3 matrix, row by row, with 0 representing the blank space):")
    for i in range(3):
        row = list(map(int, input().split()))
        goal_state.append(row)
   
    return start_state, goal_state

# Example Usage
start_state, goal_state = get_input()
visited = set()

# Get the solution using DFS
solution_path = dfs_8_puzzle(start_state, goal_state, visited, [])

# Print all states in the solution path
if solution_path:
    print("Solution path found:")
    current_state = start_state
    for move in solution_path:
        zero_pos = [(i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0][0]
        dx, dy = moves[move]
        x, y = zero_pos[0] + dx, zero_pos[1] + dy
        new_state = [row[:] for row in current_state]
        new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][zero_pos[1]]
       
        print("Move:", move)
        print_puzzle(new_state)
        current_state = new_state
else:
    print("No solution found.")
