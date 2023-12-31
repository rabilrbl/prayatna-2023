# Graph question 2

"""
Given a graph, find all possible paths between two nodes.
Start node and target node are given.

Sample Input:
[(0,0), (3,3)] # Start node, target node
[
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 2]
]

Sample Output:

[
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)],
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2), (2, 3), (3, 3)],
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)],
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3)]
]

Solution:
1. Start bfs from the start node, target node and the graph
2. For each node in the queue, keep incrementing the path
3. If the target node is found, print the path from queue
"""