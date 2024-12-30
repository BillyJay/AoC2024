file = open("input2.txt").read().strip()

lines = file.split('\n')

ans = 0
for l in lines:
	l = l.split()
	l = list(map(int, l))
	ok = False
	if (l==sorted(l) or l==sorted(l,reverse = True)): ok = True
	d = all([1<= abs(l[i] - l[i+1])<=3 for i in range(len(l)-1)])
	if ok and d:
		ans += 1
print(ans)