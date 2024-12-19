
file = open("input19.txt").read().strip()
lines = file.split('\n\n')

types = []
for line in lines[0].split('\n'):
	for el in line.split(','):
		types.append(el.strip())


memo = {}
def is_word(line):
	if line in memo: return memo[line]
	if line =="": return 1
	result = 0
	for el in types:
		if(line.startswith(el)):
			result += is_word(line[len(el):])	
	memo[line] = result
	return result

ans = 0
for line in lines[1].split('\n'):
	ans += is_word(line)
print(ans)