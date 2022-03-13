import os
from pathlib import Path
import sys
sys.path.append('../../')
"""Classes used throughout project"""
class DirectoryInformation():

        """this class stores the main direcotry of file extensions and their corresponding folder names along with the special conditions list and the method to add special conditions
        """

        """This class wil store the file extensions that will be filtered into folders as well as any keywords that must be filtered"""        
        # directory of extensions to filter based on the filetype
        info = 1
        def __init__(self):
            self.special_cases = {}


        extensions = {
                "HTML": [".html5", ".html", ".htm", ".xhtml"],
                "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                        ".heif", ".psd"],
                "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                        ".qt", ".mpg", ".mpeg", ".3gp"],
                "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                        ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                        ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                        "pptx"],
                "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                        ".dmg", ".rar", ".xar", ".zip"],
                "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                        ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
                "PLAINTEXT": [".txt", ".in", ".out"],
                "PDF": [".pdf"],
                "PYTHON": [".py"],
                "XML": [".xml"],
                "EXE": [".exe"],
                "SHELL": [".sh"]
        }

        # the following remaps the dictionary of extensions made earleir into key value pairs that can be used to identify each individual file extension and tie it to the corresponding file type
        
        FILE_FORMATS = {file_extension: format_name
            for format_name, file_formats in extensions.items()
            for file_extension in file_formats}
        
        
        
        def add_condition(self, folder_name, character):
                """this method allows the user to add a special condition to filter items with a particular character into a folder with the name 'folder_name'

                Args:
                    folder_name (string): name of the folder
                    character (string): keyword to look for in the name of files
                """                
                # updates the special_cases dictionary with the added special cases
                temp_dict = {character:folder_name}
                self.special_cases.update(temp_dict)
