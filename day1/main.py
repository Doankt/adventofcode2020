def two_mul(filename):
	with open(filename, "r") as f:
		resdict = dict()

		line = f.readline()
		while line:
			resdict[int(line)] = 2020 - int(line)
			line = f.readline()

		for k, v in resdict.items():
			if v in resdict:
				return k*v
		return -1

def three_mul(filename):
	with open(filename, "r") as f:
		resdict = dict()

		numlist = list()
		line = f.readline()
		while line:
			numlist.append(int(line))
			line = f.readline()

		for num1 in numlist:
			diff = 2020 - num1
			innerdict = dict()
			for num2 in numlist:
				if num2 < diff:
					innerdict[num2] = diff - num2
			resdict[num1] = innerdict

		for item in resdict.items():
			print(item)

		for k1, idict in resdict.items():
			for num in numlist:
				if num in idict.keys() and idict[num] in numlist:
					print(k1, num, idict[num])
					return k1*num*idict[num]
				

if __name__ == "__main__":
	print(two_mul(r"./day1/input.txt"))
	print(three_mul(r"./day1/input.txt"))