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

def find_path(graph, solution_index, start_state, path):
	if graph[solution_index] != start_state:
		path.insert(0, graph[solution_index])
		if solution_index % 9 == 0 and solution_index > 0:
			new_index = solution_index // 9 - 1
		else:
			new_index = solution_index // 9
		find_path(graph, new_index, start_state, path)
	else:
		path.insert(0, start_state)
	return path


def run_bfs(start_state):
	stack = [start_state,[]]
	# explored = {}
	graph = {0: start_state}
	solution_counter = -1
	counter = 0

	while len(stack) > 0:
		state = stack[0]
		# print(state)
		stack.pop(0)
		if len(state) == 0:
			stack.append(state)
		else:
			val = getStateVal(state)
			solution_counter += 1
			if val == 0:
				break
			# if val not in explored:
			# 	explored[val] = True
			for i in range(len(state)):
				for j in range(len(state)):
					new_state = toggle(state, i, j)
					stack.append(new_state)
					counter = counter + 1
					graph[counter] = new_state
	print(counter)
	print(solution_counter)
	# print(graph)
	solution = find_path(graph, solution_counter, start_state, [])
	print(solution)

run_bfs([[1,1,0],[0,1,1],[1,1,0]])