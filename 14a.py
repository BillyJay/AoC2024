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

for iter in range(100):
	for idx, _ in enumerate(robs):
		robs[idx][0] += robs[idx][2]
		robs[idx][1] += robs[idx][3]
		robs[idx][0] = (robs[idx][0] +R)%R
		robs[idx][1] = (robs[idx][1] +C)%C

ans = [[0,0],[0,0]]

for rob in robs:
	posi = rob[0]
	posj = rob[1]
	if (posi < (R-1)//2 and posj < (C-1)//2): 
		ans[0][0]+=1
	if (posi < (R-1)//2 and posj > (C-1)//2): 
		ans[0][1]+=1
	if (posi > (R-1)//2 and posj < (C-1)//2): 
		ans[1][0]+=1
	if (posi > (R-1)//2 and posj > (C-1)//2): 
		ans[1][1]+=1


print(ans[0][0]*ans[0][1]*ans[1][0]*ans[1][1])