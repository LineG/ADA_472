# Line Ghanem 27280076
# Anthony Iatropoulos 40028246
# Mikael Samvelian 40003178


def getNodeVal(node) -> int:
	"""Function that converts a node to an integer.
	Ex: [[0,0,0],[1,0,1],[0,1,0]] -> 1*0 + 2*0 + 4*0 + 8*1 + 16*0 + 32*1 + 64*0 + 128*1 + 256*0 -> 168

	Args:
			node: The node to be converted to a value.

	Returns:
			The return value. Integer representation of node.
	"""
	val = 0
	base = 1
	for row in range(len(node)):
		for col in range(len(node[0])):
			val += base * node[row][col]
			base = base * 2
	return val