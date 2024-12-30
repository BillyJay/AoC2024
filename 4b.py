file = open("input4.txt").read().strip()
lines = file.split('\n')

R = len(lines)
C = len(lines[0])

ans = 0

for i in range(R):
	for j in range(C):
		if (lines[i][j] == 'A'):
			if (i-1>=0 and j-1>=0 and j+1<C and i+1 < R):
				if (lines[i-1][j-1] =='M' and lines[i+1][j+1]=='S' and lines[i-1][j+1]=='S' and lines[i+1][j-1]=='M'): ans+=1
				if (lines[i-1][j-1] =='S' and lines[i+1][j+1]=='M' and lines[i-1][j+1]=='S' and lines[i+1][j-1]=='M'): ans+=1
				if (lines[i-1][j-1] =='M' and lines[i+1][j+1]=='S' and lines[i-1][j+1]=='M' and lines[i+1][j-1]=='S'): ans+=1
				if (lines[i-1][j-1] =='S' and lines[i+1][j+1]=='M' and lines[i-1][j+1]=='M' and lines[i+1][j-1]=='S'): ans+=1
print(ans)