import json
import csv
import os
import lib_rearrange

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

    match_key = ["matchId", "gameMode", *top_100, *jun_100, *mid_100, *arc_100, *util_100, *top_200, *jun_200, *mid_200, *arc_200, *util_200]
    w.writerow(match_key)

    # values
    for i in range(len(filename)):
        match = read_json(filename[i])
        # match_data = lib_rearrange.rearrange().stats(match)
        p1, p2 ,p3, p4, p5, p6, p7, p8, p9, p10 = lib_rearrange.rearrange().stats(match)
        
        matchid = match['metadata']['matchId']
        mode = match['info']['gameMode']
        w.writerow([matchid, mode, *p1, *p2, *p3, *p4, *p5, *p6, *p7, *p8, *p9, *p10])
        print(f"{filename[i]} is recorded...")
    
    print("\n####################################################\n")
    print(f"Recording is completed!!\nTotal: {len(filelist)} files\nType: {match['info']['gameMode']}")
    print("\n####################################################\n")

