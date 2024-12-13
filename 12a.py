import collections

vis = collections.defaultdict()
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



if __name__=="__main__":

	file = open("input12.txt").read().strip()
	lines = file.split('\n')
	field = [[x for x in line.strip()] for line in lines]

	R = len(field)
	C = len(field[0])

	area = collections.defaultdict()
	p = collections.defaultdict()

	label = 1
	for i in range(R):
		for j in range(C):
			dfs(i,j,field,label)
			label = label+1

	for i in range(R):
		for j in range(C):
			if not vis[(i,j)] in area: area[vis[(i,j)]] = 0
			if not vis[(i,j)] in p: p[vis[(i,j)]] = 0
			area[vis[(i,j)]] += 1
			if i+1==R or (0<= i+1 <R and vis[(i+1,j)]!=vis[(i,j)] ):
				p[vis[(i,j)]] += 1
			if j+1==C or (0<= j+1 <C and vis[(i,j+1)]!=vis[(i,j)]):
				p[vis[(i,j)]] += 1
			if i-1==-1 or (0<= i-1 <R and vis[(i-1,j)]!=vis[(i,j)]):
				p[vis[(i,j)]] += 1
			if j-1==-1 or (0<= j-1 <C and vis[(i,j-1)]!=vis[(i,j)]):
				p[vis[(i,j)]] += 1


	ans = 0
	for el in area:
		ans += area[el]*p[el]
	print(ans)