import pyperclip as pc

def pr(x):
	print(x)
	pc.copy(x)

file = open("input25.txt").read().strip() 
lines = file.split('\n\n')


all_hash = ['#','#','#','#','#']
all_dots = ['.','.','.','.','.']


ans = 0
locks = []
keys = []
for block in lines:
	field = [[el for el in l.strip()] for l in block.split('\n')]
	R = len(field)
	C = len(field[0])


	if field[0] == all_hash:
		locks.append(field)
	if field[0] == all_dots:
		keys.append(field)


ans = 0
for k in keys:
	for l in locks:
		wrong = False
		for i in range(len(k)):
			for j in range(len(k[0])):
				if(k[i][j] == '#' and  l[i][j]  == '#'):
					wrong = True 
		if(not wrong):
			ans+=1
pr(ans)