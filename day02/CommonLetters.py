#!/usr/bin/python

import sys
from bisect import insort

def create_id_list(file):
	ids = []
	
	for line in file:
		ids.append(line.strip())
	
	return ids

def get_single_mismatch_index(id1, id2):
	mismatch_count = 0
	mismatch_index = -1
	
	for j in range(0, len(id1)):
		if id1[j] != id2[j]:
			mismatch_count = mismatch_count + 1
			if mismatch_count == 1:
				mismatch_index = j
			elif mismatch_count > 1:
				return -1
				
	return mismatch_index

def get_common_letters(ids):
	for id1 in ids:
		ids.remove(id1)
		for id2 in ids:
			mismatch_index = get_single_mismatch_index(id1, id2)
		
			if mismatch_index != -1:
				return id1[:mismatch_index] + id1[(mismatch_index + 1):]
	
	return None

def common_letters(file):
	ids = create_id_list(file)
	
	return get_common_letters(ids)					

if __name__ == '__main__':
	filename = sys.argv[1] if len(sys.argv) == 2 else 'input.csv'

	with open(filename) as file:
		print(common_letters(file))