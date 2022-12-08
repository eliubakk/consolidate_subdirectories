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

    def has_children():
        return bool(children)

    # def moveTo(dest):
    #     prefix = (" " * 4 * self.getlevel()) + ("|--" if self.parent else "")
    #     (prefix + self.data)
    #     if self.children:
    #         for child in self.children:
    #             child.moveTo()
    #     else
    #         os.

    def printt(self):
        prefix = (" " * 4 * self.getlevel()) + ("|--" if self.parent else "")
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printt()

class FileSystemTree:
    def __init__(self, _root, _dest, _filetype):
        self.root = TreeNode(_root)
        self.dest = _dest
        self.filetype = _filetype
        self.__createTree(self.root)
    
    def __createTree(self, node):
        subdirectories = os.listdir(node.data)
        for directory in subdirectories:
            if (os.path.isfile(node.data + '/' + directory) and directory.endswith(self.filetype)):
                child = TreeNode(node.data + '_' + directory)
                child.parent = node
                node.add_child(child)
            elif (os.path.isdir(node.data + '/' + directory)):
                child = TreeNode(node.data + '/' + directory)
                child.parent = node
                node.add_child(child)
        for children in node.children:
            if os.path.isdir(children.data):
                self.__createTree(children)

    # def moveToDest():
    #     self.root.moveTo(self.dest)

    def printt(self):
        self.root.printt()

