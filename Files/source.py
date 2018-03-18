import os as file_sys
import sys

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

			if print_flag:
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


print_flag = 1

if len(sys.argv) == 2 and (sys.argv[1] == '-a' or sys.argv[1] == '--answer'):
	print_flag = 0
elif len(sys.argv) == 2:
	print('ERROR!')
	exit()

files = [file for file in file_sys.listdir()]
files.sort()

for file in files:
	if file_sys.path.isdir(start + '/' + file):
		if print_flag:
			print(file, '--->')

		print(ReadAllFiles(start + '/' +  file))
