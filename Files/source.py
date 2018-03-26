#/usr/bin/python3

import os
import sys
import argparse

mask = '.txt'
start = os.getcwd()
flag = 1

def ReadFile(file, op):
	count = (0 if op == '+' else 1)

	with open(file, 'r') as fin:
		for i in fin.readline().strip().split():
			if op == '+':
				count += int(i)
			else:
				count *= int(i)

	return count

def CalcRes(deway, spis):
	ret = (0 if str(deway[-1:-4:-1]) == 'dda' else 1)

	for i in spis:
                if str(deway[-1:-4:-1]) == 'dda':
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
		spis.append(ReadFile(way + '/' + file, '+' if str(way[-1:-4:-1]) == 'dda' else '*'))

def ReadAllFiles(way):
	spis = []

	for file in os.listdir(way):
		if os.path.isdir(way + '/' + file):
			isDir(way + '/' + file, spis)
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
		if os.path.isdir(start + '/' + file):
			if flag:
				print(file, '--->')

			print(ReadAllFiles(start + '/' + file))




flag = CheckProcIn()
FindStartDir()
