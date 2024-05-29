import unittest
import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from unique_word_count import unique_word_count

class TestUniqueWordCount(unittest.TestCase):
    def test_unique_word_count_is_empty(self):
        wordDict = unique_word_count()
        self.assertTrue(wordDict)
    def test_unique_word_count_test(self):
        wordDict = unique_word_count()
        self.assertEqual(wordDict["stegadon"], 3)
        self.assertEqual(wordDict["a"], 3)
        self.assertEqual(wordDict["those"], 1)
unittest.main()