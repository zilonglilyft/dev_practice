class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

"""
Use dynamic programming to loop and print the elements of the tree
"""

def pre_order(root):
    if root:
        print(root.data, end = ",")
        pre_order(root.lchild)
        pre_order(root.rchild)


a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
root = e

pre_order(root)