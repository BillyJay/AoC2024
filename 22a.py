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
nums = []
for line in lines:
	if(line==''): continue
	x = int(line)
	for _ in range(2000):
		x = op(x)
	ans += x
print(ans)