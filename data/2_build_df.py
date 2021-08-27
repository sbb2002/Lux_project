import json
import csv
import os
import lib_rearrange

myid = "고츄장떡"

# Filename
filename = []
filelist = os.listdir(f'data/gameMode/CLASSIC/overall')

for i in range(len(filelist)):
    if filelist[i] != "game_record.csv":
        name, _ = filelist[i].split('.')
        filename.append(name)
        
# Read json file
def read_json(filename):
    with open(f'data/gameMode/CLASSIC/overall/{filename}.json', 'r', encoding='utf-8') as f:
        record = json.load(f)
        return record

with open('data/gameMode/CLASSIC/overall/game_record.csv', 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    
    # key
    keys = read_json(filename[0])['info']['participants'][0].keys()
    keys = [key for key in keys]

    me_100 = [f'{key}' for key in keys]

    top_100 = [f'100TOP_{key}' for key in keys]
    jun_100 = [f'100JUN_{key}' for key in keys]
    mid_100 = [f'100MID_{key}' for key in keys]
    arc_100 = [f'100ARC_{key}' for key in keys]
    util_100 = [f'100UTIL_{key}' for key in keys]
    
    top_200 = [f'200TOP_{key}' for key in keys]
    jun_200 = [f'200JUN_{key}' for key in keys]
    mid_200 = [f'200MID_{key}' for key in keys]
    arc_200 = [f'200ARC_{key}' for key in keys]
    util_200 = [f'200UTIL_{key}' for key in keys]

    match_key = ["matchId", "gameMode", "gameDuration", *me_100, *top_100, *jun_100, *mid_100, *arc_100, *util_100, *top_200, *jun_200, *mid_200, *arc_200, *util_200]
    w.writerow(match_key)

    earlySurr = 0
    # values
    for i in range(len(filename)):
        match = read_json(filename[i])

        if match['info']['participants'][0]['gameEndedInEarlySurrender'] == True:
            print(f":: {filename[i]} was early surrendered. It will be not recorded.")
            earlySurr += 1
            continue

        # match_data = lib_rearrange.rearrange().stats(match)
        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = lib_rearrange.rearrange().stats(match)
        
        if p1[74] == myid:
            myData = p1
        if p2[74] == myid:
            myData = p2
        if p3[74] == myid:
            myData = p3
        if p4[74] == myid:
            myData = p4
        if p5[74] == myid:
            myData = p5
        if p6[74] == myid:
            myData = p6
        if p7[74] == myid:
            myData = p7
        if p8[74] == myid:
            myData = p8
        if p9[74] == myid:
            myData = p9
        if p10[74] == myid:
            myData = p10

        gameDuration = match['info']['gameDuration'] / 1000

        matchid = match['metadata']['matchId']
        mode = match['info']['gameMode']
        w.writerow([matchid, mode, gameDuration, *myData, *p1, *p2, *p3, *p4, *p5, *p6, *p7, *p8, *p9, *p10])
        print(f"{filename[i]} is recorded...")
    
    print("\n####################################################\n")
    print(f"Recording is completed!!\nTotal: {len(filelist)-1} files\nEarly surrendered: {earlySurr}\nRecord: {len(filelist)-earlySurr-1}\nType: {match['info']['gameMode']}")
    print("\n####################################################\n")

