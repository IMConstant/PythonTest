import os as file_sys
import random
import sys

start = file_sys.getcwd()

dirs = ['add', 'mul']
num = 0

def CheckAllDirs(deway):
	global num
	global rndflag
	global max_num

	for file in file_sys.listdir(deway):
		if file_sys.path.isdir(deway + '/' + file):
			rnddf = random.randint(0, 10)

			if rnddf <= rndflag:
				CreateDir(deway + '/' + file)
				CheckAllDirs(deway + '/' + file)

			for j in range(1, random.randint(2, 10)):
				fout = open(deway + '/' + file + '/file' + str(num) + '.txt', 'w')

				for i in range(5):
					fout.write(str(random.randint(1, max_num)))
					fout.write(' ')

				fout.close()
				num += 1


def CreateDir(deway):
	global dirs

	file_sys.mkdir(deway + '/' + str(random.choice(dirs)))


random.seed()

max_num = 32
rndflag = 9

for file in file_sys.listdir():
	if file_sys.path.isdir(file):
		file_sys.system('rm -rf ' + file)

if len(sys.argv) == 2 and (sys.argv[1] == '-lt' or sys.argv[1] == '--lowtests'):
	rndflag = 7
	max_num = 8
elif len(sys.argv) == 2:
	print('ERROR!')
	exit()

for i in range(20):
	way = start + '/test' + str(i)
	file_sys.mkdir(way)
	CreateDir(way)
	CheckAllDirs(way)

