def seatnum(filename):
	with open(filename, "r") as f:
		row_dict = dict()
		max_id = -1

		for i in range(128):
			row_dict[i] = [i*8 + j for j in range(8)]
		
		line = f.readline().strip("\n")
		while line:
			row_str = line[:7]

			row_val = [i for i in range(128)]
			for r in row_str:
				if r == 'F':
					row_val = row_val[:len(row_val)//2]
				elif r == 'B':
					row_val = row_val[len(row_val)//2:]
			row_val = row_val[0]

			col_str = line[7:]
			col_val = [i for i in range(8)]
			for c in col_str:
				if c == 'L':
					col_val = col_val[:len(col_val)//2]
				elif c == 'R':
					col_val = col_val[len(col_val)//2:]
			col_val = col_val[0]

			if row_dict[row_val][col_val] >= max_id:
				max_id = row_dict[row_val][col_val]
			line = f.readline().strip("\n")
		return max_id

def seatnum2(filename):
	with open(filename, "r") as f:
		row_dict = dict()
		res_list = list()

		for i in range(128):
			row_dict[i] = [i*8 + j for j in range(8)]
		
		line = f.readline().strip("\n")
		while line:
			row_str = line[:7]

			row_val = [i for i in range(128)]
			for r in row_str:
				if r == 'F':
					row_val = row_val[:len(row_val)//2]
				elif r == 'B':
					row_val = row_val[len(row_val)//2:]
			row_val = row_val[0]

			col_str = line[7:]
			col_val = [i for i in range(8)]
			for c in col_str:
				if c == 'L':
					col_val = col_val[:len(col_val)//2]
				elif c == 'R':
					col_val = col_val[len(col_val)//2:]
			col_val = col_val[0]

			res_list.append(row_dict[row_val][col_val])
			line = f.readline().strip("\n")

		res_list.sort()
		last = res_list[0]
		for x in res_list:
			if abs(last - x) > 1:
				return x - 1
			else:
				last = x
		return -1

if __name__ == "__main__":
	f = r"./day5/input.txt"
	print(seatnum(f))
	print(seatnum2(f))