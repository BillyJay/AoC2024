import collections
import heapq


file = open("input18.txt").read().strip() 
lines = file.split('\n')

R = 71
C = 71


def in_bounds(i,j):
	return 0<=i<R and 0<=j<C

d4 = [[-1,0],[1,0],[0,1],[0,-1]]

coords = []
for line in lines:
	line = line.strip()
	if(line == ""): continue
	j = int(line.split(',')[0])
	i = int(line.split(',')[1])
	coords.append([i,j])
	



def dijkstra(posi, posj,field,maxt):
	dist = collections.defaultdict()
	q = []
	heapq.heappush(q,(0,(posi,posj)))
	dist[(posi,posj)] = 0
	done = collections.defaultdict(lambda:False)
	while(len(q)):
		cur_dist, current = heapq.heappop(q)
		if(done[current]): continue
		done[current] = True
		i, j = current
		for direction_idx, direction in enumerate(d4):
			ni = i + direction[0]
			nj = j + direction[1]
			
			if not in_bounds(ni,nj): continue
			if field[ni][nj] == '#': cost = 1000000000
			else: cost = 1
			if (ni,nj) not in dist or dist[current]+cost < dist[(ni,nj)]:
				new_dist = dist[current]+cost
				dist[(ni,nj)] = new_dist
				heapq.heappush(q,(new_dist,(ni,nj)))
	return dist


field = [['.' for _ in range(R)] for _ in range(C)]

maxt = 2906
for t in range(maxt):
	ci, cj = coords[t]
	field[ci][cj] = '#'

dist = dijkstra(0,0,field,maxt)
print(coords[maxt-1][1],coords[maxt-1][0])
print(maxt, dist[(70,70)])
