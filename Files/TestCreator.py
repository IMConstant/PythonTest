#/usr/bin/python3

import os
import random
import shutil
import argparse

start = os.getcwd()

dirs = ['add', 'mul']
num = 0

def Creator(deway, file_count):
	rnddf = random.randint(0, 10)

	if rnddf <= rndflag:
		CreateDir(deway)
		file_count = CreateNext(deway, file_count)

	return CreateFiles(deway, file_count)

def CreateFiles(deway, file_count):
	for j in range(1, random.randint(2, 10)):
		fout = open(os.path.join(deway, 'file' + str(file_count) + '.txt'), 'w')

		for i in range(5):
			fout.write(str(random.randint(1, max_num)))
			fout.write(' ')

		fout.close()
		file_count += 1

	return file_count


def CreateNext(deway, file_count):
	for file in os.listdir(deway):
		if os.path.isdir(os.path.join(deway, file)):
			file_count = Creator(os.path.join(deway, file), file_count)

	return file_count

def CreateDir(deway, flg = False):
	if not flg:
		if random.randint(1, 2) == 2:
			for file in dirs:
				os.mkdir(os.path.join(deway, file))

			return

	os.mkdir(os.path.join(deway, str(random.choice(dirs))))

def CreateStartDirs(file_count):
	for i in range(1, amount + 1):
        	way = os.path.join(start, 'test' + (('0' + str(i)) if i < 10 else str(i)))
        	os.mkdir(way)
        	CreateDir(way, True)
        	file_count = CreateNext(way, file_count)

def CheckProcIn():
	parser = argparse.ArgumentParser()
	parser.add_argument('-lt', '--lowtests', action = 'store_true', help = 'low tests answers')
	parser.add_argument('-a', '--amount', action = 'store', help = 'tests amount')

	args = []

	if parser.parse_args().lowtests:
		args = [4, 5]
	else:
		args = [32, 6]

	if parser.parse_args().amount:
		args.append(int(parser.parse_args().amount))
	else:
		args.append(20)

	return args

def DeleteTests():
	for file in os.listdir():
       		if os.path.isdir(file) and file[:4] == 'test':
                	shutil.rmtree(file, ignore_errors = True)

random.seed()

DeleteTests()
max_num, rndflag, amount = CheckProcIn()
CreateStartDirs(num)
