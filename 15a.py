def push(field, d, posi, posj):
	posi_orig = posi
	posj_orig = posj
	field_cp = [[el for el in l] for l in field]
	if d=='>': dd = [0,1]
	if d=='<': dd = [0,-1]
	if d=='v': dd = [1,0]
	if d=='^': dd = [-1,0]
	if field[posi+dd[0]][posj+dd[1]]=='.':
		field_cp[posi][posj] = '.'
		field_cp[posi+dd[0]][posj+dd[1]] = '@'
		return field_cp, posi+dd[0], posj+dd[1]
	if field[posi+dd[0]][posj+dd[1]]=='#':
		return field, posi, posj
	
	insert = '@'
	new_posi = posi
	new_posj = posj
	field_cp[posi][posj] = '.'
	posi += dd[0]
	posj += dd[1]
	while(True):
		if (field_cp[posi][posj] == '#'): return field, posi_orig, posj_orig
		if (field_cp[posi][posj] == '.'): 
			field_cp[posi][posj] = insert
			if(insert =='@'):
				new_posi = posi
				new_posj = posj
			return field_cp, new_posi, new_posj
		if (field_cp[posi][posj] == 'O'): 
			field_cp[posi][posj] = insert
			if(insert =='@'):
				new_posi = posi
				new_posj = posj
			insert = 'O'
			posi += dd[0]
			posj += dd[1]
	


if __name__=='__main__':
	file = open("input15.txt").read().strip() 
	lines = file.split('\n\n')

	field = [[el for el in l.strip()] for l in lines[0].split('\n')]
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
			if field[i][j] =='O': ans += 100*(i)+j
	print(ans)