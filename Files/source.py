#/usr/bin/python3

import os
import sys
import argparse

mask = '.txt'
start = os.getcwd()
flag = 1

def ReadFile(file_way, op):
	count = (0 if op == '+' else 1)

	with open(file_way, 'r') as fin:
		for i in fin.readline().strip().split():
			if op == '+':
				count += int(i)
			else:
				count *= int(i)

	return count

def CalcRes(deway, spis):
	ret = (0 if os.path.split(deway)[1] == 'add' else 1)

	for i in spis:
                if os.path.split(deway)[1] == 'add':
                        ret += i
                else:
                        ret *= i

	return ret

def isDir(deway, spis):
	result = ReadAllFiles(deway)

	if result != 'NONE':
        	spis.append(result)

	if flag:
		print(deway, '---->', result)

def isFile(way, file, spis):
	if file.endswith(mask):
		spis.append(ReadFile(os.path.join(way, file), '+' if os.path.split(way)[1] == 'add' else '*'))

def ReadAllFiles(way):
	spis = []

	for file in os.listdir(way):
		if os.path.isdir(os.path.join(way, file)):
			isDir(os.path.join(way, file), spis)
		else:
			isFile(way, file, spis)

	if (len(spis) == 0):
		return 'NONE'
	else:
		return CalcRes(way, spis)

def CheckProcIn():
	parser = argparse.ArgumentParser()

	parser.add_argument('-a', '--answer', action = 'store_true', help = 'clear answer')

	if parser.parse_args().answer:
		return 0
	else:
		return 1

def FindStartDir():
	files = [file for file in os.listdir()]
	files.sort()

	for file in files:
		if os.path.isdir(os.path.join(start, file)):
			if flag:
				print(file, '--->')

			print(ReadAllFiles(os.path.join(start, file)))




flag = CheckProcIn()
FindStartDir()
