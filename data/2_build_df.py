import json
import csv
import os

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

# Rearrange columns
def rearrange(match):
    matchid = match['metadata']['matchId']
    mode = match['info']['gameMode']
    match_record = match['info']['participants']
    stats = [match_record[num] for num in range(10)]
    match_data = [matchid, mode, *stats]
    return match_data

    # if os.path.exists(f'data/gameMode/CLASSIC/overall/csv') == False:
    #     os.mkdir('data/gameMode/CLASSIC/overall/csv')

    # with open(f'data/gameMode/CLASSIC/overall/csv/{filename}.csv', 'w', encoding='utf-8') as f:
    #     w = csv.writer(f)
    #     w.writerow([matchid])
    #     w.writerow([mode])
    #     w.writerow(stats)
    # for player in range(10):
        # if match['info']['participants'][player]['summonerName'] == whoRU:
            # print(f"{whoRU} is {player} P.")
            # 0 1 2 3 4 == 100
            # 5 6 7 8 9 == 200
            # TOP JUN MID CAR UTIL == teamId
            # date, gameMode, p1 ~ p10 record


with open('data/gameMode/CLASSIC/overall/game_record.csv', 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    match_key = ["matchId", "gameMode", "100TOP", "100JUN", "100MID", "100ARC", "100UTIL", "200TOP", "200JUN", "200MID", "200ARC", "200UTIL"]
    w.writerow(match_key)
    for i in range(len(filename)):
        match = read_json(filename[i])
        match_data = rearrange(match)
        w.writerow(match_data)
