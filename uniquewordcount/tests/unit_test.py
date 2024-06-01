'''Unit tests'''
import unittest
import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from unique_word_count import unique_word_counter

test_file_file_path = os.path.join(current_dir, 'test_file.txt')

class TestUniqueWordCount(unittest.TestCase):
    '''Unit tests'''
    def test_unique_word_count_is_empty(self):
        word_dict = unique_word_counter(test_file_file_path, False, False)
        self.assertTrue(word_dict)
    def test_unique_word_count_test(self):
        word_dict = unique_word_counter(test_file_file_path, False, False)
        self.assertEqual(word_dict["stegadon"], 3)
        self.assertEqual(word_dict["a"], 3)
        self.assertEqual(word_dict["those"], 1)

unittest.main()
