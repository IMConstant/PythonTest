import os as file_sys
import random

start = file_sys.getcwd()

dirs = ['add', 'mul']
num = 0

def CheckAllDirs(deway):
	global num

	for file in file_sys.listdir(deway):
		if file_sys.path.isdir(deway + '/' + file):
			rnddf = random.randint(0, 10)

			if rnddf <= 9:
				CreateDir(deway + '/' + file)
				CheckAllDirs(deway + '/' + file)

			for j in range(1, random.randint(2, 10)):
				fout = open(deway + '/' + file + '/file' + str(num) + '.txt', 'w')

				for i in range(5):
					fout.write(str(random.randint(1, 32)))
					fout.write(' ')

				fout.close()
				num += 1


def CreateDir(deway):
	global dirs

	file_sys.mkdir(deway + '/' + str(random.choice(dirs)))

random.seed()

for i in range(20):
	way = start + '/test' + str(i)
	file_sys.mkdir(way)
	CreateDir(way)
	CheckAllDirs(way)

