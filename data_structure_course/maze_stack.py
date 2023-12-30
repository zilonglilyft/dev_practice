"""
The maze problem:
setup: a 2-d array, where 1 denote walls, and 0 denotes roads. Define a start and end points, then find
ways to get the end from the start。

Solution 1: use stack to do DFS (depth first search). Logics:
(1) use stack to store the route node
(2) at each node, find the next step with a defined fixed order (e.g. up, right, down, left)
(3) if reaching dead end, return the most recent node with alternative route by using stack pop feature
(4) dead end means either a wall node or a node that already in stack
=> This will not return the quickest way out
"""
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

def maze_path(x1,y1,x2,y2):
    """
    :param x1: start point x axis
    :param y1: start point y axis
    :param x2: end point x axis
    :param y2: end point y axis
    :return:
    """
    stack = []
    stack.append((x1,y1))
    while(len(stack)>0): # still try to find the end point
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2: # find the end
            for i in stack:
                print(i)
            return True
        for dir in dirs: # try different directions
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0: # good to go
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # denote the node has already checked
                break
        else: # no way out
            maze[curNode[0]][curNode[1]] = 2
            stack.pop()
    else: # stack become empty, there is no solution
        print("no way out!")
        return False

maze_path(1,1,8,8)


