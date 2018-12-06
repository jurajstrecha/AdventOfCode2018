#!/usr/bin/python

import unittest
from Checksum import get_line_metrics

class ChecksumTests(unittest.TestCase):
	def test_empty_string_input(self):
		self.assertEqual(get_line_metrics(''), (False, False))

	def test_single_character_input(self):
		self.assertEqual(get_line_metrics('a'), (False, False))

	def test_single_pair(self):
		self.assertEqual(get_line_metrics('aa'), (True, False))

	def test_single_triplet(self):
		self.assertEqual(get_line_metrics('aaa'), (False, True))
		
	def test_pair_and_triplet(self):
		self.assertEqual(get_line_metrics('abcdbefbfg'), (True, True))
		
	def test_pair_unsorted(self):
		self.assertEqual(get_line_metrics('abcdbefg'), (True, False))
		
	def test_triplet_unsorted(self):
		self.assertEqual(get_line_metrics('abcdbebfg'), (False, True))
		
	def test_quadruplet(self):
		self.assertEqual(get_line_metrics('abcdbefbgbh'), (False, False))
		
	def test_pair_last_in_alphabet(self):
		self.assertEqual(get_line_metrics('axbxc'), (True, False))
		
	def test_triplet_last_in_alphabet(self):
		self.assertEqual(get_line_metrics('axbxcxd'), (False, True))

	def test_multiple_pairs(self):
		self.assertEqual(get_line_metrics('axbxcydy'), (True, False))
		
	def test_multiple_triplets(self):
		self.assertEqual(get_line_metrics('axbxcxdyeyfyg'), (False, True))

if __name__ == '__main__':
	unittest.main()