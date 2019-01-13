import os
path='/home/alessandro/Politecnico/b) Magistrale - Computer Science and Engineering/2) Architettura del calcolatore e sistemi operativi/TE AXO'
fileList=os.listdir(path)

for file in fileList:
    for year in range(2005,2020):
        if str(year) in file:
            renamedFile=str(year)+') '+ file
            os.rename(os.path.join(path,file),os.path.join(path,renamedFile))
# prova
