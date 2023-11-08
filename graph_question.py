# Graph question 1

"""
Question appeared in Surya Software technical interview.

Consider a battlefield of size 4x4. 

The battlefield is represented as a 2D array of integers. 

Cell with value 1 represents a hero,
cell with value 2 represents a villain.

There shall be only one hero and multiple villains.

The hero can move in 4 directions: up, down, left, right.

You need to find the shortest distance between the hero and the villain.

If there are multiple villains, return the distance to the nearest villain.

Sample Input 1:
[
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 0]
]

Sample Output 1:
2

Sample Input 2:
[
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 2]
]

Sample Output 2:
2

"""


# Solution
# 1. Find the hero's position, that will be the starting point
# 2. Consider target as "2", represents the villain
# 3. Use BFS to find the shortest distance between the hero and the villain
# 4. Print the shortest distance


def find_hero_distance(grid):
    if not grid:
        return None

    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                return (x, y)

    return None


def bfs(grid, start, target):
    if not grid or not start or not target:
        return None

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    queue = [(start[0], start[1], 0)]
    # up, down and right left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y, distance = queue.pop(0)
        visited[x][y] = True

        if grid[x][y] == target:
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] != 1:
                queue.append((nx, ny, distance + 1))

    return None


def main():
    battlefield = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    start_node = find_hero_distance(battlefield)

    print(f"Hero's position is: {start_node}")

    distance = bfs(battlefield, start_node, target=2)

    print(f"Shortest distance from hero to villain is: {distance}")


if __name__ == "__main__":
    main()
