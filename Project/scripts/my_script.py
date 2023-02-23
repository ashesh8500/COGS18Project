"""Script to run some part of my project."""

# This adds the directory above to our Python path
# This is so that we can add import our custom python module code into this script
# note to the grader: forth multiple attempts, i am unable to mkae this work with a realtive path below
# hence when using it update the path with the updated filepath
import sys
sys.path.append('../')
from my_module.functions import interface
# Imports


if __name__ == 'scripts.my_script':
    interface()

pass
