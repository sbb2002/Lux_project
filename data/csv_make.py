import csv
import os
import json

filelist = os.listdir('data/overall')

def make_csv(filename):
        with open(f'data/csv/{filename}.csv', 'w', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(match['info']['participants'][0].keys())
            for player in range(10):
                w.writerow(match['info']['participants'][player].values())
    
        print(f"{filename}.csv was written successfully.")

def make_readme(match):
    with open('data/csv/readme.md', 'w') as f:
        info = match['info']['participants'][0]
        infoTypes =  [type(v) for v in info.values()]
        infoKeys = [k for k in info.keys()]
        for num in range(len(info)):
            line = str(num) + "\t" + str(infoTypes[num]) + "\t" + str(infoKeys[num]) + "\n"
            f.write(line)

for i in range(len(filelist)):
    filename = os.path.splitext(filelist[i])
    filename = filename[0]

    with open(f'data/overall/{filename}.json', 'r') as f:
        match = json.load(f)

    make_csv(filename)
# make_readme(match)



print("Making .csv is finished!!")