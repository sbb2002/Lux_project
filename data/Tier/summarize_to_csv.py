import csv
import json
import os, glob, logging, datetime

# Logging
logging.basicConfig(
    format='[%(levelname)s] %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger()
file_handler = logging.FileHandler(f'D:/PythonWorkspace/gitrepo/report_player_csv.log')
logger.addHandler(file_handler)


# Load path
def summarize(tier, division):
    directory = f'.\\data\\Tier\\{tier}\\{division}\\overall\\*.json'
    path = glob.glob(directory)
    rank = f'{tier}-{division}'
    num = len(path)
    
    with open(f'D:/PythonWorkspace/gitrepo/report_csv.log', 'r') as log:
        islog = len(log.read())

    # Write csv
    logger.info(f"[{datetime.datetime.now()}] Start writting: {rank}\t{num} files")
    with open(f'D:/PythonWorkspace/gitrepo/data_by_rank_v2.csv', 'a', encoding='euc-kr', newline='') as f:
        w = csv.writer(f, delimiter=',')            

        # Define and write key columns
        # TOP_n = f"{champName}, {k}, {d}, {a}, {cs}"
        # object_n = f"{baron}, {dragon}, {herald}"

        if islog == 0:
            team1keys = ["player_1", "player_2", "player_3", "player_4", "player_5", "bdht_1", "win_1"]
            team2keys = ["player_6", "player_7", "player_8", "player_9", "player_10", "bdht_2", "win_2"]
            keys =["matchId", "gameVersion", "rank", *team1keys, *team2keys]
            w.writerow(keys)

        # Write match values
        for i in range(num):
            with open(path[i], 'r', encoding='cp949') as f:
                js = json.load(f)

                # earlySurrendered
                if js['info']['participants'][0]['gameEndedInEarlySurrender'] == True:
                    logger.info(f"[{datetime.datetime.now()}] Pass: {rank} #{i+1}/{num}")
                    continue

                matchId = js['metadata']['matchId']
                gameVersion = js['info']['gameVersion']

                # playerData
                for j in range(10):
                    championName = js['info']['participants'][j]['championName']
                    lane = js['info']['participants'][j]['individualPosition']
                    kills = js['info']['participants'][j]['kills']
                    deaths = js['info']['participants'][j]['deaths']
                    assists = js['info']['participants'][j]['assists']
                    cs = js['info']['participants'][j]['totalMinionsKilled'] + js['info']['participants'][j]['neutralMinionsKilled']

                    if js['info']['participants'][j]['teamId'] == 100:
                        if j == 0:
                            player_1 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 1:
                            player_2 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 2:
                            player_3 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 3:
                            player_4 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 4:
                            player_5 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                    elif js['info']['participants'][j]['teamId'] == 200:
                        if j == 5:
                            player_6 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 6:
                            player_7 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 7:
                            player_8 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 8:
                            player_9 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 9:
                            player_10 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                
                # teamsData
                for j in range(2):
                    baron = js['info']['teams'][j]['objectives']['baron']['kills']
                    dragon = js['info']['teams'][j]['objectives']['dragon']['kills']
                    herald = js['info']['teams'][j]['objectives']['riftHerald']['kills']
                    tower = js['info']['teams'][j]['objectives']['tower']['kills']
                    win = js['info']['teams'][j]['win']

                    if js['info']['teams'][j]['teamId'] == 100:
                        object_1 = f"{baron}, {dragon}, {herald}, {tower}"
                        win_1 = f"{win}"
                    else:
                        object_2 = f"{baron}, {dragon}, {herald}, {tower}"
                        win_2 = f"{win}"

                values = [matchId, gameVersion, rank, player_1, player_2, player_3, player_4, player_5, object_1, win_1, player_6, player_7, player_8, player_9, player_10, object_2, win_2]

                w.writerow(values)
            print(f"[{i+1}/{num}] Written: {rank}")
    logger.info(f"[{datetime.datetime.now()}] End writting: {rank}\t{num}files")


def sum_player(summonerName):
    directory = r'data\gameMode\CLASSIC\overall\*.json'
    path = glob.glob(directory)
    num = len(path)
    
    with open(f'D:/PythonWorkspace/gitrepo/report_player_csv.log', 'r') as log:
        islog = len(log.read())

    # Write csv
    logger.info(f"[{datetime.datetime.now()}] Start writting: {summonerName}'s match data")
    with open(f'D:/PythonWorkspace/gitrepo/player_data.csv', 'a', encoding='euc-kr', newline='') as f:
        w = csv.writer(f, delimiter=',')

        # Define and write key columns
        # TOP_n = f"{champName}, {k}, {d}, {a}, {cs}"
        # object_n = f"{baron}, {dragon}, {herald}"

        if islog == 0:
            team1keys = ["player_1", "player_2", "player_3", "player_4", "player_5", "bdht_1", "win_1"]
            team2keys = ["player_6", "player_7", "player_8", "player_9", "player_10", "bdht_2", "win_2"]
            keys =["matchId", "gameVersion", "player_lane", *team1keys, *team2keys]
            w.writerow(keys)

        # Write match values
        for i in range(num):
            with open(path[i], 'r', encoding='utf-8') as f:
                js = json.load(f)

                # earlySurrendered
                if js['info']['participants'][0]['gameEndedInEarlySurrender'] == True:
                    logger.info(f"[{datetime.datetime.now()}] Pass: Because of early surrendered game")
                    continue

                matchId = js['metadata']['matchId']
                gameVersion = js['info']['gameVersion']

                # playerData
                for j in range(10):
                    position = js['info']['participants'][j]['summonerName']
                    if position == summonerName:
                        player_position = j+1
                    championName = js['info']['participants'][j]['championName']
                    lane = js['info']['participants'][j]['individualPosition']
                    kills = js['info']['participants'][j]['kills']
                    deaths = js['info']['participants'][j]['deaths']
                    assists = js['info']['participants'][j]['assists']
                    cs = js['info']['participants'][j]['totalMinionsKilled'] + js['info']['participants'][j]['neutralMinionsKilled']

                    if js['info']['participants'][j]['teamId'] == 100:
                        if j == 0:
                            player_1 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 1:
                            player_2 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 2:
                            player_3 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 3:
                            player_4 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 4:
                            player_5 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                    elif js['info']['participants'][j]['teamId'] == 200:
                        if j == 5:
                            player_6 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 6:
                            player_7 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 7:
                            player_8 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 8:
                            player_9 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                        elif j == 9:
                            player_10 = f"{championName}, {lane}, {kills}, {deaths}, {assists}, {cs}"
                
                # teamsData
                for j in range(2):
                    baron = js['info']['teams'][j]['objectives']['baron']['kills']
                    dragon = js['info']['teams'][j]['objectives']['dragon']['kills']
                    herald = js['info']['teams'][j]['objectives']['riftHerald']['kills']
                    tower = js['info']['teams'][j]['objectives']['tower']['kills']
                    win = js['info']['teams'][j]['win']

                    if js['info']['teams'][j]['teamId'] == 100:
                        object_1 = f"{baron}, {dragon}, {herald}, {tower}"
                        win_1 = f"{win}"
                    else:
                        object_2 = f"{baron}, {dragon}, {herald}, {tower}"
                        win_2 = f"{win}"

                values = [matchId, gameVersion, player_position, player_1, player_2, player_3, player_4, player_5, object_1, win_1, player_6, player_7, player_8, player_9, player_10, object_2, win_2]

                w.writerow(values)
            print(f"[{i+1}/{num}] Written.")
    logger.info(f"[{datetime.datetime.now()}] End writting: {summonerName}\t{num}files")



###################################################################
sum_player("고츄장떡")

# if os.path.exists('D:/PythonWorkspace/gitrepo/data_by_rank_v2.csv') == True:
#     os.remove('D:/PythonWorkspace/gitrepo/data_by_rank_v2.csv')
#     os.remove('D:/PythonWorkspace/gitrepo/report_csv.log')



# D1 = summarize("DIAMOND", "I")
# D2 = summarize("DIAMOND", "II")
# D3 = summarize("DIAMOND", "III")
# D4 = summarize("DIAMOND", "IV")

# P1 = summarize("PLATINUM", "I")
# P2 = summarize("PLATINUM", "II")
# P3 = summarize("PLATINUM", "III")
# P4 = summarize("PLATINUM", "IV")

# G1 = summarize("GOLD", "I")
# G2 = summarize("GOLD", "II")
# G3 = summarize("GOLD", "III")
# G4 = summarize("GOLD", "IV")

# S1 = summarize("SILVER", "I")
# S2 = summarize("SILVER", "II")
# S3 = summarize("SILVER", "III")
# S4 = summarize("SILVER", "IV")

# B1 = summarize("BRONZE", "I")
# B2 = summarize("BRONZE", "II")
# B3 = summarize("BRONZE", "III")
# B4 = summarize("BRONZE", "IV")


