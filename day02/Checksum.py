#!/usr/bin/python

import sys

def y(letter_list):
	flags = [False, False]
	list_size = len(letter_list)
	pair_found = False;
	triplet_found = False;
	
	if list_size < 2:
		return flags

	third_previous = None
	second_previous = None
	previous = None
	
	for current in letter_list:
		if previous is not None:
			if third_previous == second_previous and second_previous == previous and not triplet_found and current != previous:
				triplet_found = True
				#print('triplet')
			elif third_previous != second_previous and second_previous == previous and not pair_found and current != previous:
				pair_found = True
				#print('pair')
				
			if pair_found:
				flags[0] = True
				pair_found = False
			if triplet_found:
				flags[1] = True
				triplet_found = False
		
		third_previous = second_previous
		second_previous = previous
		previous = current
	
	if pair_found:
		flags[0] = True
		pair_found = False
	if triplet_found:
		flags[1] = True
		triplet_found = False
	
	return flags

def x(letter_list):
	flags = [False, False]
	list_size = len(letter_list)
	last_letter = ''
	pair_found = False
	
	for i in range(list_size):
		current_letter = letter_list[i]
		if current_letter == last_letter:
			if pair_found:
				flags[1] = True
				pair_found = False
			else:
				pair_found = True
				
		else:
			if pair_found:
				flags[0] = True
			pair_found = False
		
		last_letter = current_letter
				
		# no need to iterate further
		if flags[0] and flags[1]:
			return flags

	if pair_found and flags[0] == False:
		flags[0] = True
			
	return flags

def get_pair_and_triplet_found_flags(sorted_letters):
	pair = False
	triplet = False
	
	occurrences = 0
	last_letter = ''
	
	for letter in sorted_letters:
		if letter == last_letter:
			occurrences = occurrences + 1
		else:
			if occurrences == 2:
				pair = True
			elif occurrences == 3:
				triplet = True
				
			if pair and triplet:
				return pair, triplet
				
			occurrences = 1
			
		last_letter = letter
		
	if occurrences == 2:
		pair = True
	elif occurrences == 3:
		triplet = True
	
	return pair, triplet

def get_line_metrics(line):
	sorted_letters = sorted(line.strip())
	
	pair, triplet = get_pair_and_triplet_found_flags(sorted_letters)
		
	return pair, triplet

def count_checksum(file):
	pairs = 0
	triplets = 0

	for line in file:
		pair, triplet = get_line_metrics(line)
		if pair:
			pairs = pairs + 1
		if triplet:
			triplets = triplets + 1

	return pairs * triplets

if __name__ == '__main__':
	filename = sys.argv[1] if len(sys.argv) == 2 else 'input.csv'

	with open(filename) as file:
		print(count_checksum(file))