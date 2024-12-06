import collections


def next_dir(d):
	if d==(-1,0): return (0,1)
	if d==(0,1): return (1,0)
	if d==(1,0): return (0,-1)
	if d==(0,-1): return (-1,0)
	assert(False)


if __name__ == '__main__':
	file = open("input6.txt").read().strip()
	lines = file.split('\n')

	R = len(lines)
	C = len(lines[0])
	field = [[lines[i][j] for j in range(C)] for i in range(R)]

	for i in range(R):
		for j in range(C):
			if field[i][j] =='^':
				field[i][j] = '.'
				posi = i
				posj = j

	posi_orig = posi
	posj_orig = posj
	d = (-1,0)

	consider = set()
	consider.add((posi,posj))
	while(True):
		posi += d[0]
		posj += d[1]
		if(posi>=R or posi<0 or posj>=C or posj < 0):
			break
		if(field[posi][posj]=='#'):
			posi -= d[0]
			posj -= d[1]
			d = next_dir(d)
			continue
		consider.add((posi,posj))
	print(len(consider))