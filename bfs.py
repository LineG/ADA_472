def getStateVal(state) -> int:
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


def run_bfs(start_node, goal_node):
	queue = [start_node,[]]
	explored = {}
	level = 0

	# Return empty path if start is equal to goal
	if start_node == goal_node:
		return []

	while len(queue) > 0:
		path = queue.pop(0)

		if level == 0:
			node = path
		else:
			try:
				node = path[-1]
			except Exception:
				node = []
				pass

		if len(node) == 0:
			level += 1
			queue.append(node)

		else:
			val = getStateVal(node)
			if val not in explored:

				# Mark node as explored
				explored[val] = True

				for row in range(len(node)):
					for col in range(len(node)):
						child = toggle(node, row, col)
						new_path = list(path)
						new_path.append(child)
						queue.append(new_path)
						if child == goal_node:
							level+=1
							print(level)
							return new_path
	# No solution found
	return []

print(run_bfs([[0,0,0],[1,0,1],[0,1,0]], [[0,0,0],[0,0,0],[0,0,0]]))