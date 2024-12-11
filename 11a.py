import collections

file = open("input11.txt").read().strip()
lines = file


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

if __name__=="__main__":
	a = []
	for line in lines.split(' '):
		if(line == ''): continue
		a.append(int(line))

	for i in range(25):
		a = apply_rule(a)
	print(len(a))