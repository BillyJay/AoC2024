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
	adj[a].append(b)
	adj[b].append(a)

valid = []
for el1 in adj:
	for el2 in adj[el1]:
		if not(el1 < el2): continue
		for el3 in adj[el1]:
			if not(el1<el2<el3): continue
			if (el3 not in adj[el1]): continue
			if not(el1.startswith('t') or el2.startswith('t') or el3.startswith('t')): continue
			valid.append([el1,el2,el3])

pr(len(valid))