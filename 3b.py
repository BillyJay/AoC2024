import re

file = open("input3.txt").read().strip()


groups = re.findall(r'mul\((\d+)\,(\d+)\)|(do\(\))|(don\'t\(\))',file)
ans = 0
on = True
for group in groups:
	g1,g2,g3,g4 = group
	if(on and g1 != ''): ans+= int(g1)*int(g2)
	if(g3 != ''): on = True
	if(g4 != ''): on = False
print(ans)