import mlrose_hiive as mlrose
import numpy as np
import matplotlib.pyplot as plt

def queens_max(position):
    n = len(position)
    attacking_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (position[i] == position[j] or 
                abs(position[i] - position[j]) == abs(i - j)):
                attacking_pairs += 1

    return (n * (n - 1)) // 2 - attacking_pairs


objective = mlrose.CustomFitness(queens_max)


problem = mlrose.DiscreteOpt(length=8, fitness_fn=objective, maximize=True, max_val=8)


T = mlrose.ExpDecay()

initial_position = np.array([4, 6, 1, 5, 2, 0, 3, 7])

best_result = mlrose.simulated_annealing(
    problem=problem,
    schedule=T,
    max_attempts=500,
    max_iters=5000,
    init_state=initial_position
)


best_state = best_result[0] 
best_fitness = best_result[1]  

print('The best position found is: ', best_state)
print('The number non attacking pair of queens: ', best_fitness)


def plot_n_queens(positions):
    n = len(positions)
    board = np.zeros((n, n))

    for col, row in enumerate(positions):
        board[row, col] = 1 

    plt.figure(figsize=(8, 8))
    plt.imshow(board, cmap='binary', extent=[0, n, 0, n])
    

    plt.xticks(np.arange(0, n, 1))
    plt.yticks(np.arange(0, n, 1))
    plt.grid(color='gray', linestyle='-', linewidth=2)
    
 
    for col, row in enumerate(positions):
        plt.text(col + 0.5, row + 0.5, '♛', fontsize=48, ha='center', va='center', color='red')

    plt.title(f'N-Queens Solution for N={n}')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.gca().invert_yaxis() 
    plt.show()

plot_n_queens(best_state)
