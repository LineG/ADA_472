def getStateVal(state):
	val = 0
	base = 1
	for i in range(len(state)):
		for j in range(len(state[0])):
			val += base * state[i][j]
			base = base * 2
	return val

def toggle_bit(bit):
	return 1 if bit == 0 else 0

def toggle(state, i, j):
	new_state = []
	for r in state:
		new_state.append([c for c in r])

	new_state[i][j] = toggle_bit(new_state[i][j])
	if i+1 < len(state):
		new_state[i+1][j] = toggle_bit(new_state[i+1][j])
	if i-1 >= 0:
		new_state[i-1][j] = toggle_bit(new_state[i-1][j])
	if j+1 < len(state[0]):
		new_state[i][j+1] = toggle_bit(new_state[i][j+1])
	if j-1 >= 0:
		new_state[i][j-1] = toggle_bit(new_state[i][j-1])

	return new_state

def find_path(parent, start, end):
		path = [end]
		while path[-1] != start:
			path.append(parent[str(path[-1])])
		path.reverse()
		return path


def run_bfs(start_state, end_state):
	stack = [start_state,[]]
	explored = {}
	parent = {}

	while len(stack) > 0:
		state = stack[0]
		# print(state)
		stack.pop(0)
		if len(state) == 0:
			stack.append(state)
		else:
			val = getStateVal(state)
			if val == 0:
				# return find_path(parent, start_state, end_state)
				break
			if val not in explored:
				explored[val] = True
				for i in range(len(state)):
					for j in range(len(state)):
						new_state = toggle(state, i, j)
						stack.append(new_state)
						parent[str(new_state)] = state
	# solution = find_path(graph, solution_counter, start_state, [])
	# print(solution)

run_bfs([[1,1,0],[0,1,1],[1,1,0]], [[0,0,0],[0,0,0],[0,0,0]])