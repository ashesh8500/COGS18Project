import os
import sys
# note: after multiple attempts and assitance from Professor Ellis, I still couln't
# get the relative file path to detect the module hence i entered the absolute path. Okease replace it
# appropriately before testing on the local computer. You can try compiling with the relative path
# by uncommenting the below comment first.
# sys.append('../')
sys.path.append('/Users/asheshkaji/Documents/University Files/COGS18/ProjectTemplate-Ashesh-Kaji/')
from pathlib import Path
from my_module.class_holder import DirectoryInformation
"""A collection of functions for doing my project."""



def organize_special(inp, directory_info):

    """This functions takes a file path as an input and runs code to filter and redirect files with special conditions mentioned in directory_info.special_cases
       to their targeted directories.

       Args:
            inp (string): the pathname of the folder
            directory_info(class): the particular directory_info containing special conditions relevant to the operation.
    """   

    print(os.scandir(inp))
    for file in os.scandir(inp):
        # loops through all the files in the direcotry given in the pathname
        if file.is_dir():
            # checks if the given pathname represents a directory (if not it cannot be filtered and organized)    
            continue
        # defines the pathname as a pathlib.Path object
        file_path = Path(file)
        special_keys = directory_info.special_cases
        for keys in list(directory_info.special_cases): 
            
            # checks whether the keywords exist within the name of the file
            if keys in os.path.basename(file_path):

                # defines a path for a new directory with a name corresponding to the keyword's folder_name
                directory_path = Path(inp).joinpath(Path(special_keys[keys]))

                # creates the directory
                directory_path.mkdir(exist_ok=True)
                # repositions the file into the newly created directory by joining the file paths
                file_path.rename(directory_path.joinpath(os.path.basename(file_path)))
                print(file_path)
                # removes any empty directories if they exist
                for dir in os.scandir():
                    try:
                        os.rmdir(dir)
                    except:
                        pass
    

def organize_general(inp):
    """function to organize based on file formats

    Parameters
    ----------
    inp : string
        path for file to organize
    """

    print(os.scandir(inp))
    for file in os.scandir(inp):
        # loops through all the files in the direcotry given in the pathname
        if file.is_dir():
            # checks if the given pathname represents a directory (if not it cannot be filtered and organized)
            continue
        file_path = Path(file)

        # separates the file extension from the file_path to check its nature
        file_extension = file_path.suffix.lower()

        # checks if the file extension exists as a file format
        if file_extension in DirectoryInformation.FILE_FORMATS:

                # defines a path for a new directory with a name corresponding to the file format's folder name 

                directory_path = Path(inp).joinpath(Path(DirectoryInformation.FILE_FORMATS[file_extension]))
                # creates a directory 
                directory_path.mkdir(exist_ok=True)
               # repositions the file into the newly created directory by joining the file paths 
                file_path.rename(directory_path.joinpath(os.path.basename(file_path)))

                for dir in os.scandir():
                        try:
                                os.rmdir(dir)
                        except:
                                pass
    


        
def interface():
    """interface function that takes input from the user based on requirement and applies functions accordingly
    """

    inp1 = input('Hello, today will mark the end of messy files. After today, you will be able to find that document quick in a time of haste and binge-watch your favorite anime right from it\'s own folder automatically!!. \n to get started choose y: [y/n]')
    file_filter_info = DirectoryInformation()
    if inp1 == 'y':
        inp2 = input('would you like to special filter?: ')
        while inp2 == 'y':
            folder_name = input('folder name: ')
            key_term = input('keyterm: ')
            file_filter_info.add_condition(folder_name, key_term)
            inp2 = input('add another condition?')

        path_info = input('Please enter the filepath of the folder to be organized: ')        

        organize_special(path_info, file_filter_info)
        organize_general(path_info)
    else:
        print('okay then, call me whenever i\'m needed')

