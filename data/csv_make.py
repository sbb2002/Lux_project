import csv
import os
import json

filelist = os.listdir('data/overall')

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