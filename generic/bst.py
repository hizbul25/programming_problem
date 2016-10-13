class Node:
	def __init__(self, data):
		self.left = None
		self.righ = None
		self.data = data

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.righ in None:
					self.righ = Node(data)
				else:
					self.righ.insert(data)
		else:
			self.data = data

	def print_tree(self):
		if self.left:
			self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()


root = Node(8)
root.insert(10)
root.insert(2)
root.insert(5)
root.insert(15)
root.insert(6)
root.insert(9)

print(root.print_tree())