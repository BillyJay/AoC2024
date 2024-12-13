import collections


def dfs(i,j,field,label):
	if (i,j) in vis: return
	vis[(i,j)] = label
	if (0<= i+1 <R and field[i+1][j]==field[i][j]):
		dfs(i+1,j,field,label)
	if (0<= j+1 <C and field[i][j+1]==field[i][j]):
		dfs(i,j+1,field,label)
	if (0<= i-1 <R and field[i-1][j]==field[i][j]):
		dfs(i-1,j,field,label)
	if (0<= j-1 <C and field[i][j-1]==field[i][j]): 
		dfs(i,j-1,field,label)


def diag(pt1, pt2):
	if (pt1[0]-pt2[0],pt1[1]-pt2[1]) in [(1,1),(1,-1),(-1,-1),(-1,1)]: return True
	return False

def get_plaq(pt1,pt2,pt3):
	xs = [pt1[0],pt2[0],pt3[0]]
	ys = [pt1[1],pt2[1],pt3[1]]
	x = min(xs, key=xs.count)
	y = min(ys, key=ys.count)
	pt = (x,y)
	plq = []
	plq.append(pt1)
	plq.append(pt2)
	plq.append(pt3)
	plq.append(pt)
	plq = sorted(plq)
	plq = tuple(plq)
	return plq



if __name__=="__main__":
	file = open("input12.txt").read().strip()
	lines = file.split('\n')

	field = [[x for x in line.strip()] for line in lines]
	R = len(field)
	C = len(field[0])


	area = collections.defaultdict()
	p = collections.defaultdict()

	vis = collections.defaultdict()
	label = 1
	for i in range(R):
		for j in range(C):
			dfs(i,j,field,label)
			label = label+1

	perimeter = collections.defaultdict(list)
	for i in range(R):
		for j in range(C):
			if not vis[(i,j)] in area: area[vis[(i,j)]] = 0
			if not vis[(i,j)] in p: p[vis[(i,j)]] = 0
			area[vis[(i,j)]] += 1
			if i+1==R or (0<= i+1 <R and vis[(i+1,j)]!=vis[(i,j)] ):
				perimeter[vis[(i,j)]].append([(i,j),(i+1,j)])
				p[vis[(i,j)]] += 1
			if j+1==C or (0<= j+1 <C and vis[(i,j+1)]!=vis[(i,j)]):
				perimeter[vis[(i,j)]].append([(i,j),(i,j+1)])
				p[vis[(i,j)]] += 1
			if i-1==-1 or (0<= i-1 <R and vis[(i-1,j)]!=vis[(i,j)]):
				perimeter[vis[(i,j)]].append([(i,j),(i-1,j)])
				p[vis[(i,j)]] += 1
			if j-1==-1 or (0<= j-1 <C and vis[(i,j-1)]!=vis[(i,j)]):
				perimeter[vis[(i,j)]].append([(i,j),(i,j-1)])
				p[vis[(i,j)]] += 1


	corners = collections.defaultdict()
	for region in perimeter:
		corners[region] = 0
		diags = 0
		counted_plaq = collections.defaultdict()
		for idx1, el1 in enumerate(perimeter[region]):
			for idx2, el2 in enumerate(perimeter[region]):
				assert(vis[el1[0]]==vis[el2[0]])
				if(idx1<=idx2): continue
				if (el1[0]==el2[0] and diag(el1[1],el2[1])): 
					plaq = get_plaq(el1[0],el1[1],el2[1])
					if(not plaq in counted_plaq):
						counted_plaq[plaq] = 1
						corners[region]+=1
					else:
						if(counted_plaq[plaq] <2):
							corners[region]+=1	
							counted_plaq[plaq]+=1

				if (el1[1]==el2[1] and diag(el1[0],el2[0])): 
					plaq = get_plaq(el1[1],el1[0],el2[0])
					if(not plaq in counted_plaq):
						counted_plaq[plaq] = 1
						corners[region]+=1
					else:
						if(counted_plaq[plaq] <2):
							corners[region]+=1
							counted_plaq[plaq]+=1

	ans = 0
	for el in area:
		ans += area[el]*corners[el]
	print(ans)