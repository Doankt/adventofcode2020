def valid_password1(filename):
	with open(filename, "r") as f:
		counter = 0

		line = f.readline()
		while line:
			splitlines = line.split(" ")
			low, high = tuple(splitlines[0].split("-"))
			letter = splitlines[1].replace(":", "")
			string = splitlines[2].replace("\n", "")

			lettercount = string.count(letter)
			if int(low) <= lettercount <= int(high):
				counter += 1
			line = f.readline()
		return counter

def valid_password2(filename):
	with open(filename, "r") as f:
		counter = 0

		line = f.readline()
		while line:
			splitlines = line.split(" ")
			pos1, pos2 = tuple(splitlines[0].split("-"))
			letter = splitlines[1].replace(":", "")
			string = splitlines[2].replace("\n", "")

			if (string[int(pos1)-1] == letter and not string[int(pos2)-1] == letter) or (not string[int(pos1)-1] == letter and string[int(pos2)-1] == letter):
				counter += 1
			line = f.readline()
		return counter

if __name__ == "__main__":
	f = r"./day2/input.txt"
	print(valid_password1(f))
	print(valid_password2(f))