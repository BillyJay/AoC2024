file = open("input10.txt").read().strip()
lines = file.split('\n')

R = len(lines)
C = len(lines[0])

all_paths = set()

def dfs(vis, field, i, j):
	if (i,j) in vis: return 0
	if(field[i][j]==9 ): ans = 1
	else: ans = 0
	if(field[i][j]!=9): vis.add((i,j))
	if(i+1<R and field[i][j]+1==field[i+1][j]):
		ans += dfs(vis,field,i+1,j)
		if (i+1,j) in vis: vis.remove((i+1,j))
	if(j+1<C and field[i][j]+1==field[i][j+1]):
		ans += dfs(vis,field,i,j+1)
		if (i,j+1) in vis: vis.remove((i,j+1))
	if(i-1>=0 and field[i][j]+1==field[i-1][j]):
		ans += dfs(vis,field,i-1,j)
		if (i-1,j) in vis: vis.remove((i-1,j))
	if(j>=0 and field[i][j]+1==field[i][j-1]):
		ans += dfs(vis,field,i,j-1)
		if (i,j-1) in vis: vis.remove((i,j-1))
	return ans


ans = 0
field = [[int(el) for el in l.strip()] for l in lines]
for i in range(R):
	for j in range(C):
		if field[i][j] ==0:
			vis = set()
			ans += dfs(vis,field, i,j)
print(ans)