import os,re
PatternRename = "\d\d-\d\d-\d\d\d\d"
PatternOrder = "_Reference_Material_+[a-zA-Z]+_"

from VTOPSorterGlobal import directories
'''for key in directories.keys():
    print(key,directories[key],sep = "  :  ")'''



def FolderFileRename():
    PatternRename = "\d\d-\d\d-\d\d\d\d"
    PatternOrder = "_Reference_Material_+[a-zA-Z]+_"
    #Renames file name in by proper date and order
    Subject_code =  "BPHY101P_LO"  #eval("r'" + input(
        #"Enter Subject Code or directory name : ") + "'")
    if Subject_code in directories.keys():
        folder_name = "G:/My Drive/VIT/" + directories[Subject_code]
    else:  # TODO : to check this part
        folder_name = Subject_code
    os.chdir(folder_name)
    for file in os.listdir():
        print(file)

    for file in os.listdir():

        date = re.findall(PatternRename, file)
        order = re.findall(PatternOrder, file)
        if order == [] or date == []:
            continue
        if file.find(date[0]) == 0:
            continue

        date = "-".join(date[0].split("-")[::-1])
        order = (order[0].split("_")[3])
        name = re.split(PatternRename, file)[1]
        print(date + "    " + order + "    " + name)
        print(file in os.listdir())
        os.renames(file, date + "    " + order + "    " + name)
        '''try:

            os.renames(file, date + "    " + order + "    " + name)
        except:
            print("Failed")
            continue'''

FolderFileRename()