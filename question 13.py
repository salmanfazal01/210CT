class Graph:
	def __init__(self): #initialize list of nodes and dictionary of neighbours
		self.nodes = []
		self.neighbours = {} #{'A': ['B'], 'B': ['A', 'C'], ...}


	def add_node(self, value, neighbour):
		self.nodes.append(value) #append new node to list of nodes

		if(value not in self.neighbours):
			self.neighbours[value] = [] #create a key if not exists

		if neighbour: #node has a neighbour, therefore, neighbour has a node
			self.neighbours[value].append(neighbour)
			self.neighbours[neighbour].append(value)

	def printValues(self):
		for key, value in self.neighbours.items():
			print(key, value)

		

graph = Graph()
graph.add_node('A', None)
graph.add_node('B', 'A')
graph.add_node('C', 'A')
graph.add_node('D', 'B')

graph.printValues()


'''
Pseudocode:

	CLASS UNWEIGHTED-GRAPH
		INITIALIZE()
			nodes <- []
			dictionary <- {}

		ADD-NODE(VALUE, NEIGHBOUR)
			newNode <- NODE(VALUE)
			
			APPEND NEIGHBOUR to dictionary key newNode
			APPEND newNode to dictionary key NEIGHBOUR
'''
