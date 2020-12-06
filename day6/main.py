def count_questions1(filename):
	with open(filename, "r") as f:
		ret = 0

		line = f.readline().strip("\n")
		while line:
			group_set = set()
			while line != "\n":
				for c in line:
					group_set.add(c)
				line = f.readline().strip("\n")
				if not line or line == "\n":
					break

			ret += len(group_set)
			line = f.readline().strip("\n")

		return ret

def count_questions2(filename):
	with open(filename, "r") as f:
		ret = 0

		line = f.readline().strip("\n")
		while line:
			group_set = set()
			group_list = list()
			while line != "\n":
				for c in line:
					group_set.add(c)

				group_list.append(set(line))

				line = f.readline().strip("\n")
				if not line or line == "\n":
					break
			
			char_counter = 0
			for c in group_set:
				if all([c in group for group in group_list]):
					char_counter += 1
			
			ret += char_counter
			line = f.readline().strip("\n")

		return ret

if __name__ == "__main__":
	f = r"./day6/input.txt"
	print(count_questions1(f))
	print(count_questions2(f))