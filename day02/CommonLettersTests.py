#!/usr/bin/python

import unittest
from CommonLetters import get_single_mismatch_index, get_common_letters

class ChecksumTests(unittest.TestCase):
	def test_empty_ids(self):
		self.assertEqual(get_single_mismatch_index('', ''), -1)

	def test_one_character_ids(self):
		self.assertEqual(get_single_mismatch_index('a', 'a'), -1)
		
	def test_identical_ids(self):
		self.assertEqual(get_single_mismatch_index('aaa', 'aaa'), -1)
		
	def test_one_difference_start(self):
		self.assertEqual(get_single_mismatch_index('aaaa', 'baaa'), 0)

	def test_one_difference_middle(self):
		self.assertEqual(get_single_mismatch_index('aaaa', 'aaba'), 2)
		
	def test_one_difference_end(self):
		self.assertEqual(get_single_mismatch_index('aaaa', 'aaab'), 3)
		
	def test_multiple_differences_index_at_start(self):
		self.assertEqual(get_single_mismatch_index('aaaa', 'bbaa'), -1)
		
	def test_multiple_differences_index_in_middle(self):
		self.assertEqual(get_single_mismatch_index('aaaa', 'abba'), -1)
		
	def test_multiple_differences_index_at_end(self):
		self.assertEqual(get_single_mismatch_index('aaaa', 'aabb'), -1)
		
	def test_list_of_three_ids_second_pair_meets(self):
		ids = ['aaaaa', 'aaaaa', 'aaaab']
		self.assertEqual(get_common_letters(ids), 'aaaa')
		
	def test_list_of_three_ids_first_pair_meets(self):
		ids = ['aaaaa', 'baaaa', 'aaaaa']
		self.assertEqual(get_common_letters(ids), 'aaaa')
		
	def test_list_of_three_different_one_mismatch_each(self):
		ids = ['aaaaa', 'aabaa', 'aacaa']
		self.assertEqual(get_common_letters(ids), 'aaaa')
		
	def test_list_of_three_ids_none_meets(self):
		ids = ['abbaa', 'baaab', 'aaaaa']
		self.assertEqual(get_common_letters(ids), None)
		
	def test_list_of_three_ids_double_mismatches(self):
		ids = ['abbaa', 'abbaa', 'aaaaa']
		self.assertEqual(get_common_letters(ids), None)
		
	def test_list_of_three_ids_double_mismatches(self):
		ids = ['aaaaa', 'abbaa', 'accaa']
		self.assertEqual(get_common_letters(ids), None)
		
	def test_list_of_four_ids_first_and_last_mismatches(self):
		ids = ['aaaaa', 'abbaa', 'abbba', 'acaaa']
		self.assertEqual(get_common_letters(ids), 'aaaa')

if __name__ == '__main__':
	unittest.main()