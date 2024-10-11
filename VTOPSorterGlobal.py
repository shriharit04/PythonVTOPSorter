import csv, os, re
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
NotesDir = config["Directory"]["NotesDir"]

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


def CreateSubjectDir():
    """
    Creates directories for each subject listed in 'Subjects.csv' file.

    For each subject, a directory is created with subdirectories for 
    assignments and reference books. It reads the subjects from 
    the 'Subjects.csv' file and creates directories in the NotesDir path.
    """
    import os, csv
    with open("Subjects.csv") as f:
        os.chdir(NotesDir)
        reader = csv.reader(f)
        for subject in list(reader)[1:]:
            if subject[1] in os.listdir():
                print(subject[1])
                continue
            else:
                os.mkdir(subject[1])
                os.mkdir(subject[1] + r"/Assignments")
                os.mkdir(subject[1] + r'/Reference books')


def FileMoverMain():
    """
    Moves files from the download directory to the respective subject folder in the Notes directory.

    It retrieves the latest 10 files from the download directory, checks if the file name contains
    a subject code, and moves the file to the corresponding subject folder if the subject code is found.
    """

    import re, shutil

    DownloadDir = r'C:\Users\Shrihari\Downloads'
    NotesDirectory = config["Directory"]["NotesDir"]
    def FileRetreiver():
        """
        Retrieves the 10 most recently modified files from the download directory.

        Returns:
            List of file paths sorted by creation time in descending order.
        """
        import glob, os

        file_type = r'\*'
        files = glob.glob(DownloadDir + file_type)
        downloaded_files = list(reversed(sorted(files, key=os.path.getctime)))
        return downloaded_files
    

    retrievedFiles =FileRetreiver()
    # print(retrievedFiles)
    for file in retrievedFiles:
        FileName = (file.split(DownloadDir)[1][1:])
        print(FileName)
        PatternSort = "_+[a-zA-Z0-9]+_+[a-zA-Z]+_"
        SubjectCode = (re.findall(PatternSort, FileName))
        if SubjectCode == []:
            break
        if SubjectCode != []:
            SubjectCode = (SubjectCode[0][1:-1])
            print(SubjectCode)
            if SubjectCode in directories.keys():
                print(file)
                # print(NotesDirectory)
                print(NotesDirectory + "\\" + directories[SubjectCode],sep="")
                shutil.move(file, NotesDirectory + "\\" + directories[SubjectCode])


def FolderFileRename():
    """
    Renames files in a folder based on the date and order pattern in the file names.

    It checks for a specific pattern in the file names and renames the files by rearranging
    the date and adding the correct order to the file names.
    """
    PatternRename = "\d\d\d\d-\d\d-\d\d"
    PatternOrder = "_Reference-Material-+[a-zA-Z]+"
    Subject_code = eval("r'" + input("Enter Subject Code or directory name : ") + "'")
    if Subject_code in directories.keys():
        folder_name = "G:/My Drive/VIT/" + directories[Subject_code]
    else:
        folder_name = Subject_code
    # print(folder_name)
    os.chdir(folder_name)

    for file in os.listdir():
        print(file)
        date = (re.findall(PatternRename, file))
        order = re.findall(PatternOrder, file)
        # print(date)
        # print(order)
        if order == [] or date == []:
            continue
        if file.find(date[0]) == 0:
            continue

        #date = "-".join(date[0].split("-")[::-1]) # reverse date
        date = date[0]
        print(order)
        order = (order[0].split("-")[2])
        # print(order)
        name = re.split(PatternRename, file)[1]
        print("Name " ,name,end="\n\n")
        print(order)
        print(date + "    " + order + "    " + name)
        try:
            os.renames(file, date + "    " + order + "    " + name)
        except:
            continue


def FileMerger():
    """
    Merges PDF files within a date range into a single PDF.

    It prompts the user to enter a subject code, start date, and end date, and then merges
    all PDF files in the corresponding subject folder that fall within the date range.
    """
    import re
    from datetime import date
    Subject = directories[input("-> Enter Subject Code : ")]
    StartDate = list(map(int, input("-> Enter Start Date DD-MM-YYYY: ").split('-')))
    StartDate = date(StartDate[2], StartDate[1], StartDate[0])
    EndDate = list(map(int, input("-> Enter End Date DD-MM-YYYY: ").split('-')))
    EndDate = date(EndDate[2], EndDate[1], EndDate[0])
    os.chdir(NotesDir + Subject)

    ReqFiles = []
    date_pattern = "^\d+-\d+-\d+\s*"
    for file in os.listdir():
        Date = re.search(date_pattern, file)
        if Date == None:
            continue
        Date = list(map(int, (Date.group().strip().split("-"))))
        Date = date(Date[0], Date[1], Date[2])
        if StartDate <= Date <= EndDate:
            ReqFiles.append(file)

    from PyPDF2 import PdfFileMerger
    merger = PdfFileMerger()

    for file in ReqFiles:
        merger.append(os.getcwd() + "/" + file)
    merger.write(input("-> Enter New PDF's name : ") + ".pdf")
    merger.close()


def Close():
    """
    Closes the program after a short delay.
    """
    print("Closing program")
    sleep(3)
    exit()


def Archive():
    """
    Archives the current semester data and resets the workspace.

    This function is currently a placeholder and needs to be implemented.
    """
    pass


if __name__ == '__main__':
    pass
