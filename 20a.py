import collections


INF = 10**20


def in_bounds(i,j):
	return 0<=i<R and 0<=j<C


file = open("input20.txt").read().strip() 
lines = file.split('\n\n')


field = [[el for el in l.strip()] for l in lines[0].split('\n')]
R = len(field)
C = len(field[0])

d4 = [[-1,0],[1,0],[0,1],[0,-1]]



for i in range(R):
	for j in range(C):
		if field[i][j]=='S':
			field[i][j]='.'
			posi = i
			posj = j
		if field[i][j]=='E':
			field[i][j]='.'
			goali = i
			goalj = j



def bfs(starti, startj):
	dist = collections.defaultdict(lambda:INF)
	q = collections.deque()
	q.append((starti,startj))
	dist[(starti, startj)] = 0
	while(len(q)!=0):
		i,j = q.popleft()
		for d in d4:
			ni = i +d[0]
			nj = j +d[1]
			if(not in_bounds(ni,nj)): continue
			if field[ni][nj] =='#': continue
			if(dist[(i,j)]+1<dist[(ni,nj)]):
				dist[(ni,nj)] = dist[(i,j)] +1
				q.append((ni,nj))
	return dist

dist_no_cheat = bfs(posi,posj)
no_cheat = dist_no_cheat[(goali,goalj)]
all_dist = []
for i in range(R):
	print(i)
	for j in range(C):
		if (field[i][j]!='#'): continue
		field[i][j] = '.'
		dist = bfs(posi,posj)
		field[i][j] = '#'
		all_dist.append(dist)
ans = 0
for el in all_dist:
	if(el[(goali,goalj)] <=no_cheat-100): ans += 1
print(ans)