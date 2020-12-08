import numpy as np
with open('Day3.txt', 'r') as fp:
    data = fp.read().splitlines()

array = [list(line) for line in data]
maze = np.array(array)
qs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def countTrees(maze, r, d):
    x, y = 0, 0
    count = 0
    while y < maze.shape[0]:
        if x >= maze.shape[1]:
            x -= maze.shape[1]
        if maze[y][x] == '#':
            count += 1
        y += d
        x += r
    return count


m = 1
for q in qs:
    m *= countTrees(maze, q[0], q[1])

print(m)