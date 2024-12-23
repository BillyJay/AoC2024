import re
import itertools
import collections
import os 
import sys


file = open("input22.txt").read().strip() 
lines = file.split('\n')


def op(x):
	res1 = ((x^(x * 64))%16777216)
	res2 = ((res1//32)^res1)%16777216
	res3 = ((res2*2048)^res2)%16777216
	return res3

def get_seq(x):
	res = [x]
	for _ in range(2000):
		x = op(x)
		res.append(x%10)
	return res

ans = 0
numbs = []
for line in lines:
	if(line==''): continue
	x = int(line)
	numbs.append(x)

def differences(s):
	res = []
	for i in range(1,len(s)):
		res.append(s[i]-s[i-1])
	return res



score = collections.defaultdict(lambda:0)
for x in numbs:
	s = get_seq(x)
	diffs = differences(s)
	seen = collections.defaultdict(lambda: False)
	for i in range(len(diffs)-4):
		window = tuple(diffs[i:i+4])
		if (window not in seen):
			seen[window] = True
			score[window] += s[i+4]
print(max(score.values()))