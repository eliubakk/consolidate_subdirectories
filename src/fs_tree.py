import os

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printt(self):
        prefix = (" " * 4 * self.getlevel()) + ("|--" if self.parent else "")
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printt()

class FileSystemTree:
    def __init__(self, _root):
        self.root = TreeNode(_root)
        self.__createTree(self.root)
    
    def __createTree(self, node):
        subdirectories = os.listdir(node.data)
        for directory in subdirectories:
            child = TreeNode(node.data + '/' + directory)
            child.parent = node
            node.add_child(child)
        for children in node.children:
            if os.path.isdir(children.data):
                self.__createTree(children)

    def printt(self):
        self.root.printt()

