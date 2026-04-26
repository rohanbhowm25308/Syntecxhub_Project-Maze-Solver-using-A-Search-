from queue import PriorityQueue

# Maze representation (0 = free path, 1 = wall)
maze = [
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

# Start and Goal positions
start = (0, 0)
goal = (4, 4)

# Heuristic function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    open_set = PriorityQueue()
    open_set.put((0 + heuristic(start, goal), start))  # (f_score, node)

    came_from = {}  # To reconstruct path

    g_score = {start: 0}

    while not open_set.empty():
        current_f, current = open_set.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Possible moves (up, down, left, right)
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
                # Check wall
                if maze[neighbor[0]][neighbor[1]] == 1:
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    open_set.put((f_score, neighbor))

    return None  # No path found


# Run the A* algorithm
path = a_star(start, goal)

if path:
    print("Shortest path from start to goal using A* algorithm:")
    print(path)
else:
    print("No path found")