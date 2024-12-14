import re
import itertools
import collections
import os 
import sys
from functools import lru_cache
from parse import *
import statistics
from string import ascii_lowercase, ascii_uppercase
from functools import cmp_to_key
import numpy as np
import math

def get_all_nums(line):
	return list(map(int,re.findall(r'(\d+|-\d+)',line)))


def image(coords):
	for i in range(103):
		for j in range(101):
			if (i,j) in coords: print("O ",end="")
			else: print("  ",end="")
		print()

file = open("input14.txt").read().strip() 
lines = file.split('\n')

R = 103
C = 101


robs = []
for line in lines:
	line = line.strip()
	if (line==''): continue
	p1,p2,v1,v2 = get_all_nums(line)
	robs.append([(p2+R)%R,(p1+C)%C,v2,v1])


run = 1
while(True):
	for idx, _ in enumerate(robs):
		robs[idx][0] += robs[idx][2]
		robs[idx][1] += robs[idx][3]
		robs[idx][0] = (robs[idx][0] +R)%R
		robs[idx][1] = (robs[idx][1] +C)%C

	most_center = 0
	for rob in robs:
		posi = rob[0]
		posj = rob[1]
		if (posj > (C-1)//4 and posj < (C-1)//2+(C-1)//4):
			most_center += 1

	# displays input and waits if more than 400 robots are in a central strip
	# keep enter pressed until you see something interesting...
	if(most_center>400): 
		coords = []
		for el in robs:
			coords.append((el[0],el[1]))
		image(coords)
		print(run)
		input()

	if(run%5000==0): print(run)

	run += 1