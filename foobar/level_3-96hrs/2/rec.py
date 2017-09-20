from fractions import Fraction

# given_matrix=[[0, 1, 2, 1], [4, 0, 7, 1], [9, 2, 0, 1], [0, 0, 0, 0]]
given_matrix=[[0, 7, 0, 5], [2, 0, 3, 0], [2, 5, 0, 0], [0, 0, 0, 0]]
len_d = len(given_matrix)

## First convert relational probability to absolute value
## and find neighbouring nodes
nodes = {key:[] for key in range(len_d)}
for i in range(len_d):
	s = sum(given_matrix[i])
	if s<1: continue
	for j in range(len_d):
		if given_matrix[i][j]>0: nodes[i].append(j)
		given_matrix[i][j] = Fraction( given_matrix[i][j] , s)


## Parse through the neighbours and differentiate between terminating paths and looping paths
terminating_paths = []
looping_paths = []

def find_nodes_from(current_path):
	future_nodes = nodes[ current_path[-1] ]
	if future_nodes:
		for node in future_nodes:
			if node not in current_path:
				find_nodes_from( current_path + [node] )
			else:
				looping_paths.append( current_path[current_path.index(node):] + [node] )
	else:
		terminating_paths.append(current_path)


find_nodes_from([0])


looped_probability = {}
for looping_path in looping_paths[::-1]:
	prob = Fraction(1,1)
	old = looping_path[0]
	for i in looping_path[1:]:
		if i in looped_probability:
			prob *= given_matrix[i][j]*prob
		else:
			prob *= given_matrix[old][i]
		old = i
	looped_probability[ looping_path[0] ] = Fraction(1 , 1-prob)

print(nodes,terminating_paths,looping_paths,looped_probability)

terminal_nodes = {key:0 for key in range(len_d)}
for terminating_path in terminating_paths:
	ans = Fraction(1,1)
	old = terminating_path[0]
	for node in terminating_path[1:]:
		if old in looped_probability:
			ans *= looped_probability[old]

		ans *= given_matrix[old][node]
		old=node
	terminal_nodes[node] = ans

print(terminal_nodes)
