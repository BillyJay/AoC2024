import collections
from functools import cmp_to_key
import sys
from itertools import permutations, combinations_with_replacement, product
from collections import deque 
from copy import deepcopy

file = open("input7.txt").read().strip()
lines = file.split('\n')


ans = 0
for idx, l in enumerate(lines):
	l = l.strip()
	lhs = l.split(':')[0]
	rhs = l.split(': ')[1]
	rhs = list(map(int,rhs.split()))
	a = ['+','*','||']
	x = product(a,repeat = len(rhs)-1)

	for y in x:
		val = rhs[0]
		for i in range(len(y)):
			if (y[i]=='||'): 
				val = int(str(val)+str(rhs[i+1]))
			if (y[i]=='+'): val += rhs[i+1]
			if (y[i]=='*'): val *= rhs[i+1]
			if(val>int(lhs)): break
		if (val == int(lhs)):
			ans += int(val)
			print(ans)
			break
print(ans)