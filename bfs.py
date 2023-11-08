def bfs(graph, start, target):
    """
    Breadth-first search algorithm.

    graph: Graph to search. 2D array.
    start: Starting node (row, col). Tuple.
    target: Target value. Integer.
    """

    # Initialize queue for BFS
    queue = []

    # Compute number of rows and columns
    rows = len(graph)
    cols = len(graph[0])

    # Initialize visited array
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Add starting node to queue
    queue.append(start)

    # Mark starting node as visited
    visited[start[0]][start[1]] = True

    # Directions to move in
    # (row, col) or (x, y) in graph
    # (0, 1) = right
    # (1, 0) = down
    # (0, -1) = left
    # (-1, 0) = up
    # (1, 1) = diagonal down-right
    # (1, -1) = diagonal down-left
    # (-1, 1) = diagonal up-right
    # (-1, -1) = diagonal up-left
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # While queue is not empty
    while queue:

        # Pop first node from queue
        x,y = queue.pop(0)

        # Mark node as visited
        visited[x][y] = True

        # If target node is found
        # You can do any kind of processing here
        # For example, return the path to the target
        # Or return the distance to the target
        if graph[x][y] == target:
            return (x, y)

        # For each direction
        for dir_x, dir_y in directions:

            # Compute new node
            new_x, new_y = (x + dir_x, y + dir_y)

            # If new node is in bounds and not visited
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:

                # Add new node to queue
                queue.append((new_x, new_y))


# Driver code
if __name__ == "__main__":

    # Graph to search
    graph = [
        [1, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0]
    ]

    # Starting node
    start = (0, 0)

    # Target node
    target = 2

    # Run BFS
    result = bfs(graph, start, target)

    # Print result
    print(result)
    