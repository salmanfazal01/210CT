class Node:
	#Initialize node and children
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None

	'''
	If the data and value are equal, don't insert, as no duplicate data
	If data is less than value, insert data to left child and vice versa
	ie. create node of children if they dont exist.
	'''
	def insert(self, data):
		if self.value == data:
			return False
		
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		
		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True

	
	'''
	If data is less than value, return and search left child
	and vice versa till base case is met, else return False.
	'''
	def find(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False


	
	#Print node then left then right	
	def preorder(self):
		if self:
			print(str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()


	#Print left then right then node
	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()			
			print(str(self.value))


	#Print left then node then right
	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()			
			print(str(self.value))
			if self.rightChild:
				self.rightChild.inorder()

	
	def inorder2(root):
	
		# Set current to root/head of tree
		cur_node = root 
		stack = [] # initialze stack
		
		while True:			
			# Reach the left most Node of the current Node
			if cur_node != None:
				stack.append(cur_node) # Append every parent node to stack			
				cur_node = cur_node.leftChild # Keep moving to the left node leaf

			else: #If current is leaf
				if(len(stack) > 0 ): #If stack is not empty
					# Pop item from list and print it
					cur_node = stack.pop()
					print (cur_node.value)
					# Set current node to poped nodes right child 
					cur_node = cur_node.rightChild 
				#Repeat while loop

				else: #If we've reached the last leaf and stack is empty
					break


class Tree():
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False
		
	def preorder(self):
		print("PreOrder")
		self.root.preorder()

	def postorder(self):
		print("PostOrder")
		self.root.postorder()

	def inorder(self):
		print("InOrder")
		self.root.inorder()

	def inorder2(self):
		print("InOrder")
		self.root.inorder2()


bst = Tree()
bst.insert(10)
bst.insert(14)
bst.insert(21)
bst.insert(8)
bst.insert(6)
bst.insert(13)
bst.insert(18)
bst.insert(7)


#bst.preorder()
#bst.inorder()
bst.inorder2()
#bst.postorder()
