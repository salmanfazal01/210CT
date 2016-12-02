class Nodes:
	def __init__(self): #initialize list of nodes and dictionary of neighbours
		self.nodes = []
		self.neighbours = {} #{'A': {'B': 2], 'B': {'A': 5, 'C': 1}, ...}


	def add_node(self, value, neighbour, weight):

		if value not in self.nodes:
			self.nodes.append(value)
			self.neighbours[value] = {} #create a key if not exists

		if neighbour is not None: #node has a neighbour, therefore, neighbour has a node
			self.neighbours[value][neighbour] = weight
			self.neighbours[neighbour][value] = weight


	def dijkstra(self, start, end):

		nodes = self.neighbours # {'A': {'B':2}, 'B': {'C':4}, ... }
		
		unvisited = {n: float('inf') for n in self.nodes} #node & distance
		unvisited[start] = 0 #set start vertex to 0
		visited = {} #list of all visited nodes
		parent = {} #predecessors

		while unvisited:
			min_node = min(unvisited, key=unvisited.get) #smallest node
			
			#for each neighbour neighbour which is notvisited
			for neighbour, dist in nodes[min_node].items(): 
				if neighbour not in visited:
					#calc disance from starting node
					new_distance = unvisited[min_node] + nodes[min_node][neighbour]
					#if calculated distance  is lesser than known distance
					if new_distance < unvisited[neighbour]:
						#update shortest distance, update parent node with cur node
						unvisited[neighbour] = new_distance
						parent[neighbour] = min_node

			#move the current node to visited from unvisited
			visited[min_node] = unvisited[min_node]
			unvisited.pop(min_node)

			#break if we've just visited destination node
			if min_node is end:
				print("Predecessors:")
				for key, value in parent.items():
					print(key, ":", value)
				print("Visited nodes: ", visited)
				break


	def printValues(self):
		print("Nodes:\n", self.nodes, "\n\nNeighbours:")
		for key, value in self.neighbours.items():
			print(key,':', value)

		

graph = Nodes()
graph.add_node('A', None, 0)
graph.add_node('B', 'A', 4)
graph.add_node('C', 'A', 2)
graph.add_node('D', 'B', 2)
graph.add_node('E', 'B', 3)
graph.add_node('F', 'C', 1)
graph.add_node('G', 'D', 6)
graph.add_node('H', 'A', 6)
graph.add_node('I', 'F', 7)
graph.add_node('E', 'F', 1)

graph.printValues()
print("")
graph.dijkstra('A', 'F')