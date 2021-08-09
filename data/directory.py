import os

filelist = os.listdir('data/overall')

for i in range(len(filelist)):
    filename = os.path.splitext(filelist[i])
    print(filename[0])