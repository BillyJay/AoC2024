import collections
import random
import pyperclip as pc


def pr(x):
	print(x)
	pc.copy(x)


file = open("input24.txt").read().strip() 
lines = file.split('\n\n')


vals = collections.defaultdict()
for line in lines[0].split('\n'):
	if line=='': continue
	line = line.strip()
	a,b = line.split(':')
	vals[a] = int(b)

cmds = collections.defaultdict()


adj = collections.defaultdict(list)
for line in lines[1].split('\n'):
	if line=='': continue
	line = line.strip()
	a,b = line.split('->')
	a = a.strip()
	b = b.strip()
	val1, op, val2 = a.split(' ')
	cmds[b] = [val1,op,val2]

def compute(a,op,b):
	if (op=='AND'):
		return a&b
	if (op=='OR'):
		return a|b
	if (op=='XOR'):
		return a^b

def pad(s,i):
	if i<10: return s+'0'
	return s

znames = [pad('z',i)+str(i) for i in range(0,46)]
xnames = [pad('x',i)+str(i) for i in range(0,45)]
ynames = [pad('y',i)+str(i) for i in range(0,45)]


def compute_val(vals, cmds):
	while not all([z in vals for z in znames]):
		
		changed= False
		for el in cmds:
			if el in vals: continue
			if cmds[el][0] not in vals: continue
			if cmds[el][2] not in vals: continue
			changed = True
			a = vals[cmds[el][0]]
			b = vals[cmds[el][2]]
			vals[el] = compute(a,cmds[el][1],b)
		l = [vals[z] for z in znames if z in vals]
		if not changed: return -1
	s = ''.join(reversed([str(vals[z]) for z in znames if z in vals]))
	return s

def mismatch_pos(n, s):
	t=bin(n)[2:].zfill(len(s))
	for i in range(1,len(s)+1):
		if(s[-i]!=t[-i]):
			return i
	return -1




vals_orig = vals.copy()
cmds_orig = cmds.copy()
smallest = 1000
"""
- set bits x and y randomly and find least signifanct bit that malfunctions
- swap faulty outputs in cmds and rerun
"""
for _ in range(1000):
	vals = vals_orig.copy()
	cmds = cmds_orig.copy()
	# swaps:
	# cmds['vcv'],cmds['z13'] = cmds['z13'],cmds['vcv']
	# cmds['z19'],cmds['vwp'] = cmds['vwp'],cmds['z19']
	# cmds['z25'],cmds['mps'] = cmds['mps'],cmds['z25']
	# cmds['cqm'],cmds['vjv'] = cmds['vjv'],cmds['cqm']
	for x in xnames:
		vals[x] = random.randint(0,1)
	for y in ynames:
		vals[y] = random.randint(0,1)
	s = compute_val(vals,cmds)
	xbit = ''.join([str(vals[x]) for x in xnames[::-1]]).zfill(len(s))
	ybit = ''.join([str(vals[x]) for x in ynames[::-1]]).zfill(len(s))
	if (int(s,2)==int(xbit,2)+int(ybit,2)):continue
	mism = mismatch_pos(int(xbit,2)+int(ybit,2),s)
	if mism < smallest:
		print("Something wrong with bit ",pad('Z',mism-1)+str(mism-1))
		print('='*50,end='\n')
		smallest = mism
		print(xbit)
		print(ybit)
		print(compute_val(vals,cmds))
		print('='*50,end='\n')
		break
if smallest==1000:
	print("All good...")