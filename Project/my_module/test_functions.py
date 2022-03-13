"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import os
from class_holder import DirectoryInformation
from functions import organize_special, organize_general, interface
##
##



def test_all():
  test_directory = 'Trial directory'
  interface('y', 'y', 'cat files', 'cat', test_directory)
  assert os.path.isdir('Trial directory/cat files')
  assert os.path.isdir('Trial directory/DOCUMENTS')
  assert os.path.isdir('Trial directory/PDF') 

if __name__ == '__main__':
  test_all()    