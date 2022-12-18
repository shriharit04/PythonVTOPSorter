def FileMoverMain():
    import re, os, shutil
    PatternSort = "_+[a-zA-Z0-9]+_+[a-zA-Z]+_"
    ParentDir = r"G:\My Drive\VIT"
    os.chdir(r'C:\Users\Shrihari\Downloads/')
    for file in sorted(os.listdir()[:10],key = os.path.getmtime):
        print(file)

        '''if SubjectCode in directories.keys():
            shutil.move(os.getcwd() + "\\" + file, ParentDir + "\\" + directories[SubjectCode])'''


import os
import time
dir_name = r'C:\Users\Shrihari\Downloads//'
def File_sorter():
    # Get list of all files only in the given directory
    list_of_files = list(filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                            os.listdir(dir_name) ))[:10]
    # Sort list of files based on last modification time in ascending order
    list_of_files = reversed(sorted( list_of_files,
                            key = lambda x: os.path.getmtime(os.path.join(dir_name, x))
                            ))
    # Iterate over sorted list of files and print file path
    # along with last modification time of file
    for file_name in list_of_files:
        file_path = os.path.join(dir_name, file_name)
        timestamp_str = time.strftime(  '%m/%d/%Y :: %H:%M:%S',
                                    time.gmtime(os.path.getmtime(file_path)))
        print(timestamp_str, ' -->', file_name)
File_sorter()