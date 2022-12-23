import re
f = open("../VTOPSorterGlobal.py", "r")
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
