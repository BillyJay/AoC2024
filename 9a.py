file = open("input9.txt").read().strip()
lines = file.split()


lst = [lines[0][i] for i in range(len(lines[0]))]


idx = 0
fin = []
for i in range(len(lst)):
	el = lst[i]
	if(i%2==0): 
		for _ in range(int(el)): fin.append(str(idx))
		idx+=1
	else: 
		for _ in range(int(el)): 
			fin.append('.')

ptr1 = 0
ptr2 = len(fin)-1
s = (len(fin)-fin.count('.'))
while(True):
	while(fin[ptr1]!='.'): 
		ptr1 +=1
	while(fin[ptr2]=='.'): 
		ptr2 -=1
	fin[ptr1] = fin[ptr2]
	ptr1+=1
	ptr2-=1
	if ptr1 > s:
		break
fin = fin[0:s+1]

ans = 0
for i in range(s):
	ans += i*int(fin[i])
print()
print(ans)
