VALID_CHAR = {'a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'}
VALID_EYE = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
VALID_NUM = {'0','1','2','3','4','5','6','7','8','9'}

def valid_passport1(filename, checks):
	with open(filename, "r") as f:
		counter = 0
		line = f.readline()
		while line:
			pass_dict = dict()
			
			while True:
				split_line = line.strip("\n").split(" ")
				parsed_lines = [(s.split(':')[0], s.split(':')[1]) for s in split_line]
				for k, v in parsed_lines:
					pass_dict[k] = v

				line = f.readline()
				if not line or line == "\n":
					break
			line = f.readline()
			
			failed = False
			for c in checks:
				if c not in pass_dict:
					failed = True
					break
			if not failed:
				counter += 1

		return counter

def valid_passport2(filename):
	with open(filename, "r") as f:
		counter = 0
		line = f.readline()
		while line:
			pass_dict = dict()
			
			while True:
				split_line = line.strip("\n").split(" ")
				parsed_lines = [(s.split(':')[0], s.split(':')[1]) for s in split_line]
				for k, v in parsed_lines:
					pass_dict[k] = v

				line = f.readline()
				if not line or line == "\n":
					break
			line = f.readline()
			
			failed = False

			if not (('byr' in pass_dict) and len(str(pass_dict['byr'])) == 4 and (1920 <= int(pass_dict['byr']) <= 2002)):
				continue
			if not (('iyr' in pass_dict) and len(str(pass_dict['iyr'])) == 4 and (2010 <= int(pass_dict['iyr']) <= 2020)):
				continue
			if not(('eyr' in pass_dict) and len(str(pass_dict['eyr'])) == 4 and (2020 <= int(pass_dict['eyr']) <= 2030)):
				continue
			
			if 'hgt' in pass_dict:
				unit = pass_dict['hgt'][-2:]
				if unit == 'cm':
					num = int(pass_dict['hgt'][:-2])
					if not(150 <= num <= 193):
						continue
				elif unit == 'in':
					num = int(pass_dict['hgt'][:-2])
					if not(59 <= num <= 76):
						continue
				else:
					continue
			else: continue

			if 'hcl' in pass_dict:
				h = pass_dict['hcl']
				if len(h) == 7 and h[0] == "#":
					for c in h[1:]:
						if c not in VALID_CHAR:
							continue
				else:
					continue
			else:
				continue

			if not ('ecl' in pass_dict and pass_dict['ecl'] in VALID_EYE):
				continue

			if 'pid' in pass_dict and len(pass_dict['pid']) == 9:
				num = pass_dict['pid']
				for c in num:
					if c not in VALID_NUM:
						continue
			else:
				continue

			print(pass_dict)
			counter += 1

		return counter


if __name__ == "__main__":
	f = r"./day4/input.txt"
	check = [
		'byr',
		'iyr',
		'eyr',
		'hgt',
		'hcl',
		'ecl',
		'pid',		
	]
	print(valid_passport1(f, check))
	print(valid_passport2(f))