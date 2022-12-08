import os
from pathlib import Path

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

    def has_children(self):
        return bool(children)

    def moveTo(self, dest, filetype):
        prefix = (" " * 4 * self.getlevel()) + ("|--" if self.parent else "")
        path = Path(self.data)
        parent_dir = os.path.split(path.parent)
        file_name = os.path.split(path)[1]
        if not os.path.isdir(self.data) and self.data.endswith(filetype):
            print("Move " + str(path) + " -> " + dest + '/' + parent_dir[1]+ '_' + file_name)
            os.rename(str(path), dest + '/' + parent_dir[1]+ '_' + file_name)
        if self.children:
            for child in self.children:
                child.moveTo(dest,filetype)

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
            if os.path.isdir(node.data + '/' + directory) or (not os.path.isdir(node.data + '/' + directory) and directory.endswith(self.filetype)):
                child = TreeNode(node.data + '/' + directory)
                child.parent = node
                node.add_child(child)
        for children in node.children:
            if os.path.isdir(children.data):
                self.__createTree(children)

    def moveToDest(self):
        self.root.moveTo(self.dest, self.filetype)

    def printt(self):
        self.root.printt()

