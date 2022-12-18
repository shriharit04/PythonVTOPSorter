import csv,os,re
from time import sleep
ParentDir = r"G:\My Drive\VIT/"
directories = {}
#Displays Subject name
with open("Subjects.csv") as File:  # To have updated variable of directories
    Reader = csv.reader(File)
    for Subject in list(Reader)[1:]:
        directories[Subject[0]] = Subject[1]
for k,v in directories.items():
    print(k,v,sep = "  :  ")

#Displays Function name
f = open("VTOPSorterGlobal.py","r")
content = f.read()
pattern = "def +[a-zA-Z0-9]+[(]"
functions = re.findall(pattern,content)
FuncDict = {}
for i in range(len(functions)):
    FuncDict[i+1] = functions[i].split()[1][:-1]
for k,v in FuncDict.items():
    print(k,v,sep = "  :  ")


def CreateSubjectDir():  # 1.0 -> no csv storage
    from os import mkdir
    from VtopDownloader import directories
    SubjectCode = input("Enter Subject code : ")
    SubjectName = input("Enter Subject name : ")
    mkdir(ParentDir + SubjectName)
    mkdir(ParentDir + SubjectName + "/Reference books")
    mkdir(ParentDir + SubjectName + "/Assignments")
    print("Created " + SubjectName)

    #Adding to csv aswell
    with open("Subjects.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow([SubjectCode,SubjectName])
    directories[SubjectCode] = SubjectName


def AddNewSubjectsFolder(SubjectCode,SubjectName):  # 2.0 -> Reads from csv storage
    import os, csv
    with open("Subjects.csv") as f:
        os.chdir(ParentDir)
        reader = csv.reader(f)
        for subject in list(reader)[1:]:
            print(subject[1])
            if subject[1] in os.listdir():
                continue
            else:
                os.mkdir(subject[1])
                os.mkdir(subject[1] + r"/Assignments")
                os.mkdir(subject[1] + r'/Reference books')



def FileMoverMain():
    import re, os, shutil
    PatternSort = "_+[a-zA-Z0-9]+_+[a-zA-Z]+_"
    NotesDirectory = r"G:\My Drive\VIT"
    os.chdir(NotesDirectory + r"\Temp material")
    for file in os.listdir():
        SubjectCode = (re.findall(PatternSort, file)[0][1:-1])
        if SubjectCode in directories.keys():
            shutil.move(os.getcwd() + "\\" + file, NotesDirectory + "\\" + directories[SubjectCode])

def FolderFileRename():
    #Renames file name in by proper date and order
    PatternRename = "\d\d-\d\d-\d\d\d\d"
    PatternOrder = "_Reference_Material_+[a-zA-Z]+_"
    Subject_code = eval("r'" + input(
        "Enter Subject Code or directory name : ") + "'")
    if Subject_code in directories.keys():
        folder_name = "G:/My Drive/VIT/" + directories[Subject_code]
    else:  # TODO : to check this part
        folder_name = Subject_code
    os.chdir(folder_name)

    for file in os.listdir():

        date = (re.findall(PatternRename, file))
        order = re.findall(PatternOrder, file)
        if order == [] or date == []:
            continue
        if file.find(date[0]) == 0:
            continue

        date = "-".join(date[0].split("-")[::-1])
        order = (order[0].split("_")[3])
        name = re.split(PatternRename, file)[1]
        print(date + "    " + order + "    " + name)
        try:

            os.renames(file, date + "    " + order + "    " + name)
        except:
            print(False)
            continue

def Close():
    print("Closing program")
    sleep(1)
    exit()

if __name__ == '__main__':
    pass
