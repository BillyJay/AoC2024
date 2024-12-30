import re

file = open("input3.txt").read().strip()


groups = re.findall(r'mul\((\d+)\,(\d+)\)',file)
ans = 0
for group in groups:
	g1,g2 = group
	if(g1!='' and g2 != ''): ans+= int(g1)*int(g2)
print(ans)