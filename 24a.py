import collections
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
	if i<10: return 'z0'
	return 'z'

znames = [pad('z',i)+str(i) for i in range(0,46)]
xnames = [pad('x',i)+str(i) for i in range(0,45)]
ynames = [pad('y',i)+str(i) for i in range(0,45)]

cmds_cp = [el for el in cmds]
while not all([z in vals for z in znames]):
	for el in cmds:
		if el in vals: continue
		if cmds[el][0] not in vals: continue
		if cmds[el][2] not in vals: continue
		a = vals[cmds[el][0]]
		b = vals[cmds[el][2]]
		vals[el] = compute(a,cmds[el][1],b)
	l = [vals[z] for z in znames if z in vals]
s = ''.join(reversed([str(vals[z]) for z in znames if z in vals]))
pr(int(s,2))