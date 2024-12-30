file = open("input1.txt").read()

lines = file.split('\n')


R = len(lines)
C = len(lines[0])
ans = 0


a = []
b = []
for line in lines:
	if(line==''): continue
	x,y = line.split()
	a.append(int(x))
	b.append(int(y))

a = sorted(a)
b = sorted(b)
ans = 0
for i in range(len(a)):
	ans += abs(a[i]-b[i])
print(ans)