import collections

file = open("input11.txt").read().strip()
lines = file


memo = collections.defaultdict()


def apply_rule(a):
	new_a = []
	for i in range(len(a)):
		done = False
		el = a[i]
		if (el==0): 
			new_a.append(1)
			done = True
		if(len(str(el))%2==0):
			x = str(el)[0:len(str(el))//2]
			y = str(el)[len(str(el))//2:]
			x = int(x)
			y = int(y)
			new_a.append(x)
			new_a.append(y)
			done = True
		if (not done):
			new_a.append(el*2024)
	a= new_a
	return a



def get_length(el,times):
	if times == 0: return len(el)

	hval = hash(tuple([*el,times]))
	if hval in memo.keys(): return memo[hval]

	length = 0 
	for x in apply_rule(el):
		length+=get_length([x],times-1)

	memo[hval] = length
	return length


if __name__=="__main__":
	a = []
	for line in lines.split(' '):
		if(line == ''): continue
		a.append(int(line))

	print(get_length(a,75))