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
