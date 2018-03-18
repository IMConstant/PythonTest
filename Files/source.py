import os as file_sys

mask = '.txt'
start = file_sys.getcwd()

def CheckFile(file, op):
	count = (0 if op == '+' else 1)

	with open(file, 'r') as fin:
		for i in fin.readline().strip().split():
			if op == '+':
				count += int(i)
			else:
				count *= int(i)

	return count

def ReadAllFiles(way):
	spis = []

	for file in file_sys.listdir(way):
		if file_sys.path.isdir(way + '/' + file):
			result = ReadAllFiles(way + '/' + file)

			if result != 'NONE':
				spis.append(result)

			print(way + '/' + file, '---->', result)

		elif file.endswith(mask):
			spis.append(CheckFile(way + '/' + file, '+' if str(way[-1:-4:-1]) == 'dda' else '*'))

	ret = (0 if str(way[-1:-4:-1]) == 'dda' else 1)

	if (len(spis) == 0):
		return 'NONE'

	for i in spis:
		if str(way[-1:-4:-1]) == 'dda':
			ret += i
		else:
			ret *= i

	return ret


for i in range(20):
	print(ReadAllFiles(start + '/test' + str(i)))
