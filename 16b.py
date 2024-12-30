import collections
import heapq


file = open("input16.txt").read().strip() 


field = [[el for el in l.strip()] for l in file.split('\n')]
R = len(field)
C = len(field[0])

d4 = [[0,-1],[1,0],[0,1],[-1,0]]


posi, posj = 0, 0
goali, goalj = 0, 0
for i in range(R):
	for j in range(C):
		if field[i][j]=='S': 
			posi,posj = i,j
			field[i][j] = '.'
		if field[i][j]=='E': 
			goali,goalj = i,j
			field[i][j] = '.'

def dijkstra(posi, posj, posdir):
	dist = collections.defaultdict(lambda:10**20)
	q = [(0,(posi,posj,posdir))]
	dist[(posi,posj,posdir)] = 0
	done = collections.defaultdict(lambda:False)
	while(len(q)):
		current = heapq.heappop(q)
		if(done[current[1]]): continue
		done[current[1]] = True
		i, j, cur_dir = current[1]
		cost = dist[current[1]]+1000
		new_dir = (cur_dir+1)%4
		if (i,j,new_dir) not in dist or cost <= dist[(i,j,new_dir)]:
			dist[(i,j,new_dir)] = cost
			heapq.heappush(q,(dist[current[1]]+1000,(i,j,new_dir)))

		new_dir = (cur_dir+3)%4
		if (i,j,new_dir) not in dist or cost <= dist[(i,j,new_dir)]:
			dist[(i,j,(cur_dir+3)%4)] = cost
			heapq.heappush(q,(dist[current[1]]+1000,(i,j,new_dir)))

		direction = d4[cur_dir]
		ni = i + direction[0]
		nj = j + direction[1]
		if field[ni][nj] == '#': continue

		cost = dist[current[1]]+1
		if (ni,nj,cur_dir) not in dist or cost <= dist[(ni,nj,cur_dir)]:	
			dist[(ni,nj,cur_dir)] = cost
			heapq.heappush(q,(cost,(ni,nj,cur_dir)))
	
	return dist

def opposite(a, b):
	if(d4[a][0]==-d4[b][0] and d4[a][1]==-d4[b][1]): return True
	return False

dist = dijkstra(posi, posj,2)
opt_cost = dist[(goali,goalj,3)]

dist_rev = dijkstra(goali, goalj,1)
coords = set()
for el1 in dist:
	for el2 in dist_rev:
		if(el1[0]==el2[0] and el1[1]==el2[1] and opposite(el1[2],el2[2]) and dist[el1]+dist_rev[el2]==opt_cost):
			coords.add((el1[0],el1[1]))
print(len(coords))