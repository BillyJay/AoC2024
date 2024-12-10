file = open("input10.txt").read().strip()
lines = file.split('\n')

R = len(lines)
C = len(lines[0])

all_paths = set()

def dfs(field, i, j):
	if(field[i][j]==9 ): ans = 1
	else: ans = 0
	if(i+1<R and field[i][j]+1==field[i+1][j]):
		ans += dfs(field,i+1,j)
	if(j+1<C and field[i][j]+1==field[i][j+1]):
		ans += dfs(field,i,j+1)
	if(i-1>=0 and field[i][j]+1==field[i-1][j]):
		ans += dfs(field,i-1,j)
	if(j>=0 and field[i][j]+1==field[i][j-1]):
		ans += dfs(field,i,j-1)
	return ans


ans = 0
field = [[int(el) for el in l.strip()] for l in lines]
for i in range(R):
	for j in range(C):
		if field[i][j] ==0:
			ans += dfs(field, i,j)
print(ans)