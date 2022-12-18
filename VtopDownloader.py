import os, shutil, re

PatternRename = "\d\d-\d\d-\d\d\d\d_"
PatternSort = "_+[a-zA-Z0-9]+_+[a-zA-Z]+_"

#TODO: Add selenium suport to automate downloading()(rewuires chcking date as well) long shot

from VTOPSorterGlobal import directories

os.chdir("G:/My Drive/VIT/Temp material")
NotesDirectory = "G:/My Drive/VIT"
print(os.getcwd())

for file in os.listdir():

    SubjectCode = (re.findall(PatternSort, file))
    if len(SubjectCode) > 0:
        SubjectCode = SubjectCode[0][1:-1]
    print(SubjectCode)

    #print(re.findall(PatternSort, file))  # gets the required SubjectCode
    if SubjectCode in list(directories.keys()):
        print(re.split(PatternRename, file))
        print("_____")
        try:
            NewName = re.split(PatternRename, file)[1]
            os.renames(file, NewName)
            shutil.move(os.getcwd() + "\\" + NewName, NotesDirectory + "\\" + directories[SubjectCode] + "\\reference material")
        except:
            shutil.move(os.getcwd() + "\\" + file,NotesDirectory + "\\" + directories[SubjectCode] + "\\reference material")


'''for folder in directories.values():
    os.chdir("G:/My Drive/VIT/" + folder + "/reference material")
    for file in os.listdir():
        print(file)
        print(re.split(PatternRename,file))
        try:
            os.renames(file,re.split(PatternRename,file)[1])
        except:
            pass'''
