file = open("input8.txt").read().strip()
lines = file.split('\n')

field = [[x for x in line.strip()] for line in lines]
field2 = [[x for x in line.strip()] for line in lines]


R = len(field)
C = len(field[0])


for i1 in range(R):
	for j1 in range(C):
		for i2 in range(R):
			for j2 in range(C):
				if (i1==i2 and j1==j2): continue
				if(field[i1][j1]==field[i2][j2] and field[i1][j1]!='.'):
					di = i2 - i1
					dj = j2 - j1
					posi = i1
					posj = j1
					while(0<=posi<R and 0<=posj<C): 
						field2[posi][posj] = '#'
						posi -= di
						posj -= dj
					posi = i2
					posj = j2
					while(0<=posi<R and 0<=posj<C): 
						field2[posi][posj] = '#'
						posi += di
						posj += dj
ans = 0
for i in range(R):
	for j in range(C):
		if(field2[i][j]=='#'): ans+=1
print(ans)