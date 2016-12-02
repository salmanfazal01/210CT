class Graph:
	def __init__(self): #initialize list of nodes and dictionary of neighbours
		self.nodes = []
		self.neighbours = {} #{'A': ['B'], 'B': ['A', 'C'], ...}


	def add_node(self, value, neighbour):
		self.nodes.append(value) #add new node to list of nodes

		if(value not in self.neighbours):
			self.neighbours[value] = [] #create dictionary key if not exists

		if neighbour: #node has a neighbour, therefore, neighbour has a node
			self.neighbours[value].append(neighbour)
			self.neighbours[neighbour].append(value)


	def bfs(self, start):
		queue = [start] #start value as first node
		visited = [] #list of the visited nodes
		
		while queue: #while queue has a value
			cur_node = queue.pop(0) #start working with the first node

			for neighbour in self.neighbours[cur_node]: #for all neighbours of the node
				if neighbour not in visited:
					queue.append(neighbour) #append to queue if not visited

			visited.append(cur_node) #append current node to visited
		return visited

		#queue: [B, C, H, E, D]
		#visited: [A, ]


	def dfs(self, start):
		stack = [start] #start value as first node
		visited = [] #list of the visited nodes
		
		while stack: #while stack has a value
			cur_node = stack.pop(0) #start working with the first node

			for neighbour in self.neighbours[cur_node]: #for all neighbours of the node
				if neighbour not in visited:
					stack.append(neighbour) #append to stack if not visited

			visited.append(cur_node) #append current node to visited
		return visited

		#[A, B, C, H, F]
		#[A, H, C, F]


	#output data to file
	def writeToFile(self, x, y):
		graph = """
    ------------A------------
    |           |           |
----B----     --C           H
|       |     |
E       D     F--
        |       |
        G       I 
		"""
		file = open("question 14.txt", "w") #open file (create if not exists)
		file.write(graph) #write graph to file
		file.write("\n\nBFS:\n%s" % x) #breadth first search sequence
		file.write("\n\nDFS:\n%s" % y) #depth fist search sequence
		file.close()

		

graph = Graph()
graph.add_node('A', None)
graph.add_node('B', 'A')
graph.add_node('C', 'A')
graph.add_node('D', 'B')
graph.add_node('E', 'B')
graph.add_node('F', 'C')
graph.add_node('G', 'D')
graph.add_node('H', 'A')
graph.add_node('I', 'F')


graph.writeToFile(graph.bfs('A'), graph.dfs('A'))
