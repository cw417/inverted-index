import sys
from pathlib import Path
from collections import defaultdict

class InvertedIndex:
  def __init__(self, directory_path: str) -> None:
    self.directory_path = Path(directory_path)
    self.file_list = self.create_file_list()
    self.terms_list = defaultdict(defaultdict(defaultdict(list))) # {term: {filename: {term_in_file: [(line_num, word_num]}}} 

  def create_file_list(self) -> [str]:
    """Creates a list of filenames from the initial diretory path."""
    file_list = []
    for file in self.directory_path.iterdir():
      if file.is_file():
        file_location = str(file.cwd()) + "/" + str(self.directory_path) + "/" + file.name
        file_list.append(file_location)
    return file_list
  
  def get_file_terms(self, file:str) -> {str: [(int, int)]}:
    """
    Reads through the specified file.
    Returns a dictionary with the form {term [(line_number, word_number)]}:
      - Key: term
      - Value: list of tuples, with the line number and word number where the term occurred in the document.
        - The word number is relative to the start of each line
    """
    terms = defaultdict(list)
    with open(file, 'r') as fp:
      data = fp.readlines()
      data = [item.rstrip('\n').split() for item in data]
      for line_number, line in enumerate(data):
        for word_number, word in enumerate(line):
          word = word.lower()
          location = (line_number, word_number)
          terms[word].append(location)
    return terms
  
  def create_terms_list(self):
    # {term: {filename: {term_in_file: [(line_num, word_num]}}}
    for file in self.file_list:
      terms = self.get_file_terms(file)
      for term, location in terms.items():
        print(term, location)

if __name__ == '__main__':
  index = InvertedIndex('test_files/')
  #print(index.get_file_terms('test_files/file1.txt'))
  index.create_terms_list()