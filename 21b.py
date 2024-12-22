import re
import itertools
import collections
from functools import lru_cache

def get_all_nums(line):
	return list(map(int,re.findall(r'(\d+|-\d+)',line)))


def press_key(key,curr_pos):
	if(curr_pos=='A'):
		ret = {'A':'A','0':'<A','1':'^<<A','2':'^<A','3':'^A','4':'^^<<A','5':'^^<A','6':'^^A','7':'^^^<<A','8':'^^^<A','9':'^^^A'}
		return ret[key]
	if(curr_pos=='0'):
		ret = {'A':'>A', '0':'A','1':'^<A','2':'^A','3':'^>A','4':'^^<A','5':'^^A','6':'^^>A','7':'^^^<A','8':'^^^A','9':'^^^>A'}
		return ret[key]
	if(curr_pos=='1'):
		ret = {'A':'>>vA','0':'>vA','1':'^A','2':'>A','3':'>>A','4':'^A','5':'^>A','6':'^>>A','7':'^^A','8':'^^>A','9':'^^>>A'}
		return ret[key]
	if(curr_pos=='2'):
		ret = {'A':'>vA','0':'vA','1':'<A','2':'A','3':'>A','4':'^<A','5':'^A','6':'^>A','7':'^^<A','8':'^^A','9':'^^>A'}
		return ret[key]
	if(curr_pos=='3'):
		ret = {'A':'vA','0':'<vA','1':'<<A','2':'<A','3':'A','4':'^<<A','5':'^<A','6':'^A','7':'^^<<A','8':'^^<A','9':'^^A'}
		return ret[key]
	if(curr_pos=='4'):
		ret = {'A':'>>vvA','0':'>vvA','1':'vA','2':'v>A','3':'>>vA','4':'A','5':'>A','6':'>>A','7':'^A','8':'^>A','9':'^>>A'}
		return ret[key]
	if(curr_pos=='5'):
		ret = {'A':'>vvA','0':'vvA','1':'v<A','2':'vA','3':'v>A','4':'<A','5':'A','6':'>A','7':'^<A','8':'^A','9':'^>A'}
		return ret[key]
	if(curr_pos=='6'):
		ret = {'A':'vvA','0':'<vvA','1':'v<<A','2':'v<A','3':'vA','4':'<<A','5':'<A','6':'A','7':'^<<A','8':'<^A','9':'^A'}
		return ret[key]
	if(curr_pos=='7'):#check
		ret = {'A':'>>vvvA','0':'>vvvA','1':'vvA','2':'vv>A','3':'vv>>A','4':'vA','5':'v>A','6':'v>>A','7':'A','8':'>A','9':'>>A'}
		return ret[key]
	if(curr_pos=='8'):#check
		ret = {'A':'>vvvA','0':'vvvA','1':'vv<A','2':'vvA','3':'vv>A','4':'v<A','5':'vA','6':'v>A','7':'<A','8':'A','9':'>A'}
		return ret[key]
	if(curr_pos=='9'):#check
		ret = {'A':'vvvA','0':'<vvvA','1':'vv<<A','2':'<vvA','3':'vvA','4':'v<<A','5':'<vA','6':'vA','7':'<<A','8':'<A','9':'A'}
		return ret[key]

def press_keys(seq):
	val = ""
	curr_pos = 'A'
	for idx,s in enumerate(seq):
		val = val + press_key(s,curr_pos)
		curr_pos = s
	return val


def press_robot(key,curr_pos):
	if(curr_pos=='A'):
		ret = {'A':'A','>':'vA','^':'<A','v':'<vA','<':'v<<A'}
		return ret[key]
	if(curr_pos=='^'):
		ret = {'A':'>A','>':'>vA','^':'A','v':'vA','<':'v<A'}
		return ret[key]
	if(curr_pos=='>'):
		ret = {'A':'^A','>':'A','^':'<^A','v':'<A','<':'<<A'}
		return ret[key]
	if(curr_pos=='<'):
		ret = {'A':'>>^A','>':'>>A','^':'>^A','v':'>A','<':'A'}
		return ret[key]
	if(curr_pos=='v'):
		ret = {'A':'>^A','>':'>A','^':'^A','v':'A','<':'<A'}
		return ret[key]

def press_robot_seq(seq):
	val = ""
	curr_pos ='A'
	for idx,s in enumerate(seq):
		val = val + press_robot(s,curr_pos)
		curr_pos = s
	return val


def get_all_perms(s):
	sequences = s.split('A')
	new_sequences = []
	
	perm_seqs = [set([''.join(p) for p in itertools.permutations(seq)]) for seq in sequences]


	all_sequences = list(itertools.product(*perm_seqs))
	
	new_sequences = [s[:]]
	for perm in all_sequences:
		sequence = 'A'.join(perm)
		new_sequences.append(sequence)
	return new_sequences

def hover(seq):
	ok = [[0,1],[0,2],[1,0],[1,1],[1,2]]
	init = [0,2]
	for s in seq:
		if(s=='>'): init[1]+=1
		if(s=='v'): init[0]+=1
		if(s=='<'): init[1]-=1
		if(s=='^'): init[0]-=1
		if(s=='A'): continue
		if init not in ok: return True
	return False

def num_key_hover(seq):
	ok = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,1],[3,2]]
	init = [3,2]
	for s in seq:
		if(s=='>'): init[1]+=1
		if(s=='v'): init[0]+=1
		if(s=='<'): init[1]-=1
		if(s=='^'): init[0]-=1
		if(s=='A'): continue
		if init not in ok: return True
	return False


@lru_cache(maxsize = 100000)
def get_min_length(s, level):
	if level==0:
		return len(s)
	
	s=s.replace('A','A.')
	parts = s.split('.')[:-1]
	res = 0
	all_factors = []
	for part in parts:
		if level!=1: factor = [el for el in get_all_perms(press_robot_seq(part)) if not hover(el)]
		else: factor = [el for el in get_all_perms(press_robot_seq(part))]
		all_factors.append(factor)
	all_sequences = list(itertools.product(*all_factors))
	best = 10**20
	for sequence in all_sequences:
		length = 0
		for part in sequence:
			length += get_min_length(part,level-1)
		best = min(best, length)
	return best


if __name__=='__main__':
	file = open("input21.txt").read().strip() 
	codes = file.split('\n')
	nums = get_all_nums(file)

	ans = 0
	for idx, code in enumerate(codes):
		to_enter = press_keys(code)
		best = 10**20
		for el_to_enter in get_all_perms(to_enter):
			if num_key_hover(el_to_enter): continue
			best = min(best, get_min_length(el_to_enter,25))
		ans += best*nums[idx]
	print(ans)