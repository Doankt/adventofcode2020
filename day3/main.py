TREE = "#"
OPEN = "."

def count_trees1(filename, right, down):
	with open(filename, "r") as f:
		line = f.readline()
		
		counter = 0
		hpos = 0		
		linelen = len(line) - 1
		while line:
			# Make movements
			hpos += right
			for _ in range(down):
				line = f.readline()
				if not line: return counter

			# Check if tree
			if line[hpos % linelen] == TREE:
				counter += 1
		
		return counter

def multi_slope(filename, slope_list):
	res = 1
	for right, down in slope_list:
		res *= count_trees1(filename, right, down)
	return res


if __name__ == "__main__":
	f = r"./day3/input.txt"
	print(count_trees1(f, 3, 1))

	s_list = [
		(1, 1),
		(3, 1),
		(5, 1),
		(7, 1),
		(1, 2)
	]

	print(multi_slope(f, s_list))