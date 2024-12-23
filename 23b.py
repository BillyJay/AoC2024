import re
import itertools
import collections
import os 
import sys
from functools import lru_cache
from parse import *
import statistics
from string import ascii_lowercase, ascii_uppercase
from functools import cmp_to_key
import numpy as np
import math
import heapq
import copy
import pyperclip as pc
import random

def pr(x):
	print(x)
	pc.copy(x)

file = open("input23.txt").read().strip()
lines = file.split('\n')


adj = collections.defaultdict(list)
for line in lines:
	if line=='': continue
	line = line.strip()
	a, b = line.split('-')
	# print(a,b)
	adj[a].append(b)
	adj[b].append(a)


d = set()
keys = list(adj.keys())
best = 0
for iter in range(10000):
	random.shuffle(keys)
	clique = []
	for el in keys:
		if el not in clique:
			ok = True
			for a in clique:
				if (a not in adj[el]):
					ok = False
					break
			if(ok): clique.append(el)
	if len(clique) > best:
		best = len(clique)
		print("best length = ",len(clique)," with sequence ",end='')
		pr(','.join(sorted(clique)))