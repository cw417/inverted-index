import unittest
from inverted_index import InvertedIndex

class TestInvertedIndex(unittest.TestCase):

  def __init__(self, methodName: str = "runTest") -> None:
    super().__init__(methodName)
    self.index = InvertedIndex('test_files/')

  def test_get_file_list(self):
    list_of_files = ['file1.txt', 'file2.txt', 'file3.txt' ]
    self.assertEqual(self.index.file_list)