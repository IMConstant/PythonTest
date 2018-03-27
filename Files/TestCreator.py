#/usr/bin/python3

import os
import random
import shutil
import argparse

start = os.getcwd()

dirs = ['add', 'mul']
num = 0

def Creator(deway):
	rnddf = random.randint(0, 10)

	if rnddf <= rndflag:
		CreateDir(deway)
		CreateNext(deway)

	CreateFiles(deway)

def CreateFiles(deway):
	global num #txt files count

	for j in range(1, random.randint(2, 10)):
		fout = open(deway + '/file' + str(num) + '.txt', 'w')

		for i in range(5):
			fout.write(str(random.randint(1, max_num)))
			fout.write(' ')

		fout.close()
		num += 1


def CreateNext(deway):
	for file in os.listdir(deway):
		if os.path.isdir(deway + '/' + file):
			Creator(deway + '/' + file)

def CreateDir(deway, flg = False):
	if flg == False:
		if random.randint(1, 2) == 2:
			os.mkdir(deway + '/add')
			os.mkdir(deway + '/mul')

			return

	os.mkdir(deway + '/' + str(random.choice(dirs)))

def CreateStartDirs():
	for i in range(1, amount + 1):
        	way = start + '/test' + (('0' + str(i)) if i < 10 else str(i))
        	os.mkdir(way)
        	CreateDir(way, True)
        	CreateNext(way)

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
CreateStartDirs()
