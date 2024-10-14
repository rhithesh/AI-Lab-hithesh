from collections import deque

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

# BFS algorithm
def bfs_8_puzzle(start, goal):
    queue = deque([(start, [])])  # Each element is (current_state, path_taken)
    visited = set()
    visited.add(puzzle_to_string(start))
    state_space_tree = []

    while queue:
        current, path = queue.popleft()

        if current == goal:
            state_space_tree.append((current, path))  # Record final state and path
            return state_space_tree  # Puzzle solved, return best path

        zero_pos = [(i, j) for i in range(3) for j in range(3) if current[i][j] == 0][0]

        for move, (dx, dy) in moves.items():
            x, y = zero_pos[0] + dx, zero_pos[1] + dy
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = [row[:] for row in current]
                new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][zero_pos[1]]

                if puzzle_to_string(new_state) not in visited:
                    visited.add(puzzle_to_string(new_state))
                    queue.append((new_state, path + [move]))  # Add move to the path
                    state_space_tree.append((new_state, path + [move]))  # Record the state and path

    return state_space_tree  # Return the entire state space tree if no solution

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

# Get the best path using BFS
solution_tree = bfs_8_puzzle(start_state, goal_state)

# Print all states in the best move sequence
if solution_tree:
    print("State space tree leading to the solution:")
    for state, moves in solution_tree:
        print("Moves taken:", moves)
        print_puzzle(state)
else:
    print("No solution found.")
