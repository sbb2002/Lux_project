import csv
import os
import json
import pickle

filelist = os.listdir('data/overall')

# csv file
for i in range(len(filelist)):
    filename = os.path.splitext(filelist[i])
    filename = filename[0]

    with open(f'data/overall/{filename}.json', 'r') as f:
        match = json.load(f)

    with open(f'data/csv/{filename}.csv', 'w', encoding='euc-kr') as f:
        w = csv.writer(f)

        for player in range(10):
            w.writerow(match['info']['participants'][player].values())
    
    print(f"{filename}.csv was writen successfully.")

print("Making .csv is finished!!")

# readme.md
with open('data/csv/readme.md', 'w') as f:
    info = match['info']['participants'][0]
    infoTypes =  [type(v) for v in info.values()]
    infoKeys = [k for k in info.keys()]
    for num in range(len(info)):
        line = str(num) + "\t" + str(infoTypes[num]) + "\t" + str(infoKeys[num]) + "\n"
        f.write(line)