import collections
from functools import cmp_to_key

file = open("input5.txt").read().strip()
lines = file.split('\n\n')



before = collections.defaultdict(list)

for l in lines[0].split('\n'):
	x,y = map(int, l.split('|'))
	before[y].append(x)

ans = 0
for l in lines[1].split('\n'):
	seq = list(map(int, l.split(',')))
	
	def comp(x,y):
		if(x in before[y]): 
			return -1
		if(y in before[x]): return 1
		return 0

	if seq==sorted(seq, key=cmp_to_key(comp)): 
		ans += seq[len(seq)//2]
print(ans)