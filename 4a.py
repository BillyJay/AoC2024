file = open("input4.txt").read().strip()
lines = file.split('\n')


R = len(lines)
C = len(lines[0])

ans = 0

for i in range(R):
	for j in range(C):
		if j+3<C: 
			s = lines[i][j]+lines[i][j+1]+lines[i][j+2]+lines[i][j+3]
			if (s=='XMAS'): ans += 1
			if (s[::-1]=='XMAS'): ans += 1
		if i+3<R: 
			s = lines[i][j]+lines[i+1][j]+lines[i+2][j]+lines[i+3][j]
			if (s=='XMAS'): ans += 1
			if (s[::-1]=='XMAS'): ans += 1
		if i+3<R and j+3<C: 
			s = lines[i][j]+lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3]
			if (s=='XMAS'): ans += 1
			if (s[::-1]=='XMAS'): ans += 1
		if i+3<R and j-3>=0: 
			s = lines[i][j]+lines[i+1][j-1]+lines[i+2][j-2]+lines[i+3][j-3]
			if (s=='XMAS'): ans += 1
			if (s[::-1]=='XMAS'): ans += 1
print(ans)