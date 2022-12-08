from fs_tree import FileSystemTree

class FileSystemCrawler:
	def __init__(self, _root, _dest, _file_type):
		self.root = _root
		self.dest = _dest
		self.file_type = _file_type
		self.dirTree = FileSystemTree(_root, _dest, _file_type)

	def preformMove(self):
		self.dirTree.moveToDest()

	def printt(self):
		self.dirTree.printt()
