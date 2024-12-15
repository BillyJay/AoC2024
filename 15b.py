def dfs(field, d, cells):
	if d=='>': dd = [0,1]
	if d=='<': dd = [0,-1]
	if d=='v': dd = [1,0]
	if d=='^': dd = [-1,0]
	new_cells = set()
	for el in cells:
		i = el[0] + dd[0]
		j = el[1] + dd[1]
		if((i,j) in cells): continue
		if(field[i][j]!='.'): new_cells.add((i,j))
		if field[i][j] == '#': return False
		if(field[i][j]=='['): 
			if not (i,j+1) in cells: new_cells.add((i,j+1))
		if(field[i][j]==']'): 
			if not (i,j-1) in cells: new_cells.add((i,j-1))
	if len(new_cells) == 0: return cells
	return dfs(field, d, cells.union(new_cells))


def push(field, d, posi, posj):
	if d=='>': dd = [0,1]
	if d=='<': dd = [0,-1]
	if d=='v': dd = [1,0]
	if d=='^': dd = [-1,0]
	
	cells = set()
	cells.add((posi, posj))
	cells = dfs(field, d, cells)

	if(cells!=False):
		field_cp = [[el for el in l] for l in field]
		for el in cells:
			i = el[0]
			j = el[1]
			field_cp[i][j] = '.'
		for el in cells:
			field_cp[el[0]+dd[0]][el[1]+dd[1]] = field[el[0]][el[1]]
		return field_cp, posi+dd[0], posj+dd[1]
	else: return field, posi, posj

def wider_field(field):
	field_cp = [['.' for _ in range(len(field[0])*2)] for _ in range(len(field))]
	R = len(field)
	C = len(field[0])

	for i in range(R):
		for j in range(C):
			if field[i][j]=='@':
				field_cp[i][2*j] = '@'
				field_cp[i][2*j+1] = '.'
			if field[i][j]=='#':
				field_cp[i][2*j] = '#'
				field_cp[i][2*j+1] = '#'
			if field[i][j]=='O':
						field_cp[i][2*j] = '['
						field_cp[i][2*j+1] = ']'
	return field_cp				


if __name__=='__main__':
	file = open("input15.txt").read().strip() 
	lines = file.split('\n\n')

	field = [[el for el in l.strip()] for l in lines[0].split('\n')]
	
	field = wider_field(field)
	R = len(field)
	C = len(field[0])

	for i in range(R):
		for j in range(C):
			if field[i][j] =='@':
				posi = i
				posj = j

	for line in lines[1].split('\n'):
		if line=='': continue
		for d in line:
			field, posi, posj = push(field, d, posi, posj)

	ans = 0
	for i in range(R):
		for j in range(C):
			if field[i][j] =='[': 
				di = min(i,R-1-i)
				dj = min(j,C-1-j)
				ans += 100*(i)+j
	print(ans)