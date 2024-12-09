file = open("input9.txt").read().strip()
lines = file.split()


lst = [lines[0][i] for i in range(len(lines[0]))]


idx = 0
fin = []
for i in range(len(lst)):
	el = lst[i]
	if(i%2==0): 
		fin.append([str(idx) for _ in range(int(el))])
		idx+=1
	else: 
		if int(el)!=0: fin.append(['.' for _ in range(int(el))])



fin2 = [el for el in fin if not '.' in el]
fin2.reverse()

for idx, el in enumerate(fin2):
	for i in range(fin.index(el)):
		if('.' in fin[i] and len(fin[i])>=len(el)):
			dots = ['.' for _ in range(len(el))]
			fin = [dots if x == el else x for x in fin]
			fin.insert(i,el)

			fin[i+1] = fin[i+1][0:-len(fin[i])]
			if(fin[i+1]==[]):
				del fin[i+1]
			break

fin_d = []
for x in fin:
	for y in list(x):
		fin_d.append(y)
fin = [x for x in fin_d]

ans = 0
for idx in range(len(fin)):
	if fin[idx]=='.': continue
	ans += idx*int(fin[idx])

print(ans)
