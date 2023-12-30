"""
The maze problem:
setup: a 2-d array, where 1 denote walls, and 0 denotes roads. Define a start and end points, then find
ways to get the end from the start。

Solution 2: use queue to do BFS (depth first search). Logics:
(1) at each node, simultaneously explore all possible way out
(2) use a queue to ONLY store the front head of each route. At each step, enqueue the next node
and dequeue the current node
(3) use another list to store the current node and its previous node, with index
(4) Once the queue reach the end point, track back the route by calling the list
=> This will return the fastest way out
"""

from collections import deque

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y: (x-1,y),
    lambda x,y: (x,y+1),
    lambda x,y: (x+1,y),
    lambda x,y: (x,y-1),
]

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])
    realpath.reverse()
    for i in realpath:
        print(i)

def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,-1))
    path = [] # store all the dequeued nodes
    while len(queue) > 0: # still has road
        curNode = queue.popleft() # deque the current node first
        path.append(curNode) # immediately append the current node to the path list
        if curNode[0] == x2 and curNode[1] == y2: # check if cur node is the end
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print('no way out')
        return False

maze_path_queue(1,1,8,8)
