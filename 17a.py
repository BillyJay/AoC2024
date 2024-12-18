file = open("input17.txt").read().strip() 
lines = file.split('\n')


def exec(A,B,C,cmd):	


	strs= ""
	def trunc(x,y):
		if(x/y>=0): return x//y
		else: return x//y +1

	ptr = 0
	cmbo = 0
	steps = 0
	while(ptr<len(cmd)):
		steps += 1
		if (0<=cmd[ptr+1]<=3): cmbo = cmd[ptr+1]
		if (cmd[ptr+1] == 4): cmbo = A
		if (cmd[ptr+1] == 5): cmbo = B
		if (cmd[ptr+1] == 6): cmbo = C
		if(cmd[ptr]==0):
			A = A//(2**cmbo)
		if(cmd[ptr]==1):
			B = B^cmd[ptr+1]
		if(cmd[ptr]==2):
			B = cmbo%8
		if(cmd[ptr]==3):
			if A!=0: 
				ptr = cmd[ptr+1]
				continue
		if(cmd[ptr]==4):
			B = B^C
		if(cmd[ptr]==5):
			strs = strs+str(cmbo%8)+','
		if(cmd[ptr]==6):
			B = A//(2**cmbo)
		if(cmd[ptr]==7):
			C = A//(2**cmbo)
		ptr += 2

	return strs[:-1]

A = int(lines[0].strip().split(': ')[1])
B = int(lines[1].strip().split(': ')[1])
C = int(lines[2].strip().split(': ')[1])
cmds = list(map(int,(lines[4].strip().split(': ')[1].split(','))))
print(exec(A,B,C,cmds))