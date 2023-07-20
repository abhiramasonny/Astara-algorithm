from GUI import start_val, end_val, walls, size
import os
import matplotlib.pyplot as plt
if not start_val or not end_val:
    raise ValueError('Start or end value not set')

def get_adjacent_squares(square, matrix, visited):
    x, y = square
    result = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]) and matrix[x + dx][y + dy] != 1 and (x + dx, y + dy) not in visited:
            result.append((x + dx, y + dy))
    return result

def a_star(matrix):
    start = start_val
    end = end_val
    if not start or not end:
        raise ValueError('Invalid matrix: no start or end square')
    heap = [((0, start))]
    visited = set()
    path = {}
    cost_hashmap = {}
    cost_hashmap[start] = 0
    
    while heap:
        cost, square = heap.pop(0)
        if square == end:
            path_reversed = []
            while square != start:
                path_reversed.append(square)
                square = path[square]
            path_reversed.append(start)
            return list(reversed(path_reversed))
        visited.add(square)
        for adj_square in get_adjacent_squares(square, matrix, visited):
            new_cost = cost + 1
            if adj_square not in cost_hashmap or new_cost < cost_hashmap[adj_square]:
                cost_hashmap[adj_square] = new_cost
                path[adj_square] = square
                heap.append((new_cost, adj_square))
        heap.sort(key=lambda x: cost_hashmap[x[1]])
    raise ValueError('No path found')


def plot_matrix_with_path(matrix, path):
    def fill_path_matrix(path, path_matrix, index=0, path_len=len(path)):
        if index == path_len:
            return
        x, y = path[index]
        path_matrix[x][y] = 1
        fill_path_matrix(path, path_matrix, index + 1, path_len)
    
    rows, cols = len(matrix), len(matrix[0])
    walls = [[matrix[i][j] == 1 for j in range(cols)] for i in range(rows)]
    path_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    fill_path_matrix(path, path_matrix)
    
    fig, ax = plt.subplots()
    ax.imshow(path_matrix, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
    ax.imshow(walls, cmap='binary', interpolation='nearest', alpha=0.5)
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        ax.add_artist(plt.Arrow(y1, x1, y2 - y1, x2 - x1, width=0.3, color='gray'))

    plt.show()



def generate_matrix():
    global start_val
    global end_val
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for wall in walls:
        x, y = wall
        matrix[x][y] = 1
    x, y = start_val
    #start val is 2
    matrix[x][y] = 2
    x, y = end_val
    #end val is 3
    matrix[x][y] = 3
    return matrix

os.system("clear")
matrix = generate_matrix()
path = a_star(matrix)
print("Shortest distence between 2 points (A* alg) is: ", len(path))
plot_matrix_with_path(matrix, path)
