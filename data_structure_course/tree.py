class Node:
    def __init__(self, name, type = 'dir'):
        self.name = name
        self.type = type # 'dir' or 'file'
        self.children = [] # use list to store all the children
        self.parent = None # point to the parent node

    def __repr__(self): # add this to print name with the print() function
        return self.name


class FileSystemTree: # proxy the linux file system
    def __init__(self):
        self.root = Node("/") # the root node is just "/"
        self.now = self.root # current level in the tree system

    def mkdir(self, name): # create new folder under current level
        if name[-1] != "/": # all the new directories should end with "/"
            name += "/"
        node = Node(name) # create new node
        self.now.children.append(node) # store the node in the children list
        node.parent = self.now # mark the parent of the new node as the current level

    def ls(self): # show all folders under current level
        return self.now.children

    def cd(self, name): # go to the upper or lower level
        if name[-1] != "/":
            name += "/"
        if name == "..":
            self.now = self.now.parent
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        else:
            raise ValueError("no such folder!")


tree = FileSystemTree()
tree.mkdir("var")
tree.mkdir("bin")
tree.mkdir("usr")
tree.cd("bin")
tree.mkdir("zilong")
print(tree.ls())

