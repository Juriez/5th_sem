from collections import defaultdict 

class Graph(): 

	# ctor to initialize
	def __init__(self, vertices): 
		self.graph = defaultdict(list) 
		self.V = vertices

	# Create a directed graph
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	def isCyclicUtil(self, v, visited, Stack): 
		visited[v], Stack[v] = True, True
		# Recur for all neighbours 
		# if any neighbour is visited and in 
		# Stack then graph is cyclic 
		for neighbour in self.graph[v]: 
			if visited[neighbour] == False: 
				if self.isCyclicUtil(neighbour, visited, Stack) == True: 
					return True
			elif Stack[neighbour] == True: 
				return True

		# The node needs to be poped from recursion Stack
		Stack[v] = False
		return False

	def isCyclic(self): 
		visited = [False] * self.V 
		Stack = [False] * self.V 
		for node in range(self.V): 
			if visited[node] == False: 
				if self.isCyclicUtil(node, visited, Stack) == True: 
					return True
		return False

	# Helper fn to topologicalSort()
	def topologicalSortUtil(self,v,visited,stack): 
		visited[v] = True
		# Recur for all the vertices adjacent to this vertex 
		for adj in self.graph[v]: 
			if visited[adj] == False: 
				self.topologicalSortUtil(adj,visited,stack) 
		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited, stack = [False]*self.V, []
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 
		return stack