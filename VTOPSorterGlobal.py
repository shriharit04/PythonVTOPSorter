import csv, os, re
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
NotesDir = config["Directory"]["NotesDir"]

# NotesDir = r"G:\My Drive\VIT/"  #config
directories = {}
# Displays Subject name
with open("Subjects.csv") as File:  # To have updated variable of directories
    Reader = csv.reader(File)
    for Subject in list(Reader)[1:]:
        directories[Subject[0]] = Subject[1]
for k, v in directories.items():
    print(k, v, sep="  :  ")

# Displays Function name
f = open("VTOPSorterGlobal.py", "r")
content = f.read()
pattern = "def +[a-zA-Z0-9]+[(]"
functions = re.findall(pattern, content)
ExceptionFn = []
FuncDict = {}
for i in range(len(functions)):
    if functions[i] in ExceptionFn:
        continue
    FuncDict[i + 1] = functions[i].split()[1][:-1]
for k, v in FuncDict.items():
    print(k, v, sep="  :  ")


def CreateSubjectDir():  # 2.0 -> Reads from csv storage
    import os, csv
    with open("Subjects.csv") as f:
        os.chdir(NotesDir)
        reader = csv.reader(f)
        for subject in list(reader)[1:]:
            print(subject[1])
            if subject[1] in os.listdir():
                continue
            else:
                os.mkdir(subject[1])
                os.mkdir(subject[1] + r"/Assignments")
                os.mkdir(subject[1] + r'/Reference books')


def FileMoverMain():  # moves files from download directory to respective folder
    import re, shutil

    DownloadDir = r'C:\Users\Shrihari\Downloads'  # config
    NotesDirectory = r"G:\My Drive\VIT"  # config

    def FileRetreiver():  # Retrieves latest 10 files from directory mentioned
        # need to understand
        import glob, os

        file_type = r'\*'
        files = glob.glob(DownloadDir + file_type)
        downloaded_files = list(reversed(sorted(files, key=os.path.getctime)))
        return downloaded_files

    for file in FileRetreiver():  # stops if it doesnt get a vtop file
        FileName = (file.split(DownloadDir)[1][1:])
        PatternSort = "_+[a-zA-Z0-9]+_+[a-zA-Z]+_"
        SubjectCode = (re.findall(PatternSort, FileName))
        if SubjectCode == []:
            break
        if SubjectCode != []:
            SubjectCode = (SubjectCode[0][1:-1])
            print(file)
            if SubjectCode in directories.keys():
                shutil.move(file, NotesDirectory + "\\" + directories[SubjectCode])


def FolderFileRename():
    # Renames file name in by proper date and order
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


def FileMerger():
    import re
    from datetime import date
    Subject = directories["BPHY101L_TH"]  # directories[input("-> Enter Subject Code : ")]
    StartDate = date(2022, 11, 11)  # list(map(int,input("-> Enter Start Date DD-MM -YYYY: ").split('-')))
    # StartDate = date(StartDate[2],StartDate[1],StartDate[0])
    EndDate = date(2022, 12, 12)  # list(map(int,input(input("-> Enter End Date DD-MM -YYYY: ").split('-'))))
    # EndDate = date(EndDate[2],EndDate[1],EndDate[0])
    os.chdir(NotesDir+Subject)
    ReqFiles = []
    date_pattern = "^\d+-\d+-\d+\s*"  # pattern for getting date
    for file in os.listdir():
        Date = re.search(date_pattern, file)
        if Date == None:
            continue
        Date = list(map(int, (Date.group().strip().split("-"))))
        Date = date(Date[0], Date[1], Date[2])
        if StartDate < Date < EndDate:
            print(file)
            ReqFiles.append(file)

    from PyPDF2 import PdfFileMerger
    merger = PdfFileMerger()

    for file in ReqFiles:
        merger.append(os.getcwd()+"/"+file)
    merger.write(input("-> Enter New PDF's name : ")+".pdf")
    merger.close()



def Close():
    print("Closing program")
    sleep(3)
    exit()


def Archive():  # stores semester archive and resets
    pass


if __name__ == '__main__':
    pass
