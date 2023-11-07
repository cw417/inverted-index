import sys
from pathlib import Path

class InvertedIndex:
  def __init__(self, directory_path) -> None:
    self.directory_path = Path(directory_path)
    self.file_list = self.get_file_list()
    
  def get_file_list(self):
    file_list = []
    for file in self.directory_path.iterdir():
      if file.is_file():
        file_list.append(file.name)
    return file_list
  
  def read_file(self, file):
    terms = {}
    with open(file, 'r') as fp:
      data = fp.readlines()
      data = [item.rstrip('\n').split() for item in data]
      # need to add dictionary value as tuple with (line, word_num) for term key
    print(data)
    return terms
  
  #def get_file_terms(self):
  #  count = 1

  #  for 

if __name__ == '__main__':
  index = InvertedIndex('test_files/')
  print(index.read_file('test_files/file1.txt'))