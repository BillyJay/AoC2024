import collections
import heapq


file = open("input16.txt").read().strip() 
lines = file.split('\n\n')


field = [[el for el in l.strip()] for l in lines[0].split('\n')]
R = len(field)
C = len(field[0])

d4 = [[-1,0],[1,0],[0,1],[0,-1]]


posi, posj = 0, 0
goali, goalj = 0, 0
for i in range(R):
	for j in range(C):
		if field[i][j]=='S': posi,posj = i,j
		if field[i][j]=='E': goali,goalj = i,j

def dijkstra(posi, posj, posdir):
	dist = collections.defaultdict()
	q = [(0,(posi,posj,posdir))]
	dist[(posi,posj,posdir)] = 0
	done = collections.defaultdict(lambda:False)
	while(len(q)):
		current = heapq.heappop(q)
		if(done[current[1]]): continue
		done[current[1]] = True
		i, j, cur_dir = current[1]
		for direction_idx, direction in enumerate(d4):
			if (direction[0],direction[1])==(-d4[cur_dir][0],-d4[cur_dir][1]): continue
			ni = i + direction[0]
			nj = j + direction[1]
			if field[ni][nj] == '#': continue
			if (direction_idx == cur_dir): cost = 1
			else: cost = 1001
			if (ni,nj,direction_idx) not in dist or dist[current[1]]+cost < dist[(ni,nj,direction_idx)]:
				new_dist = dist[current[1]]+cost
				dist[(ni,nj,direction_idx)] = new_dist
				heapq.heappush(q,(new_dist,(ni,nj,direction_idx)))
	return dist

dist = dijkstra(posi, posj,2)

print(dist[(goali,goalj,0)])