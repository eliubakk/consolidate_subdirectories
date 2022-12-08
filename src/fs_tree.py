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
        self.__createTree()
    
    def __createTree(self):
        subdirectories = os.listdir(self.root.data)
        for directory in subdirectories:
            child = TreeNode(directory)
            child.parent = self.root
            self.root.add_child(child)

    def printt(self):
        self.root.printt()

