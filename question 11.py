#class to create nodes, each node will have a link to the previous and the next node
class node:
	def __init__(self, data):
		self.data = data
		self.next_node = None
		self.prev_node = None


#class where users can access functions to use nodes
class linked_list:
	def __init__(self):
		self.root = None #this will store lists first element
	
	#add a new node to the linked list
	def add_node(self, data):
		new_node = node(data) #instance

		#roots previous node links to itself.
		if(self.root != None):
			self.root.prev_node = new_node

		#insert to the start of the list, so root will be the new node and
		#previous root will be the next node
		new_node.next_node = self.root
		self.root = new_node

	#delete node from list
	def del_node(self, data):
		cur_node = self.root #start using root

		#while current holds a node/value
		while cur_node != None:
			if cur_node.data == data: #if data found
				next = cur_node.next_node #link to its next node
				prev = cur_node.prev_node #link to its previous node

				if next != None: #if next node exists
					next.prev_node = prev #set its next node to link to prev node
				
				if prev != None: #if previous node exists
					prev.next_node = next #set prev node to link to next node
				else:
					self.root = cur_node.next_node #make the root to be next node

				return True #true if node successfully deleted
			
			else: #if data is not root
				cur_node = cur_node.next_node #move to the next node
		
		return False #return false if node not found

	#print linked list
	def print_list(self):
		node = self.root

		while node:
			print(node.data)
			node = node.next_node


newList = linked_list()
newList.add_node(1)
newList.add_node(2)
newList.add_node(3)

newList.del_node(3)

newList.print_list()
