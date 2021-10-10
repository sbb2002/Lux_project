import requests, time
import pandas as pd
from package import apikey

api_key = apikey.apikey()
url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}

def getId(summonerName):
    url4id = url + summonerName
    id = requests.get(url4id, headers=headers).json()['id'] 
    return id

def getPuuid(summonerName):
    url4puuid = url + summonerName
    puuid = requests.get(url4puuid, headers=headers).json()['puuid'] 
    return puuid

def getTier(summonerName):
    url4id = url + summonerName
    id = requests.get(url4id, headers=headers).json()['id']
    url4tier = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id
    tier = requests.get(url4tier, headers=headers).json()[0]['tier']   
    return tier

def getMatchlist(puuid):
    url4matchlist = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?type=ranked&start=0&count=20"
    matchlist = requests.get(url4matchlist, headers=headers).json()
    return matchlist

def getData(summonerName, matchlist):
    team1keys = ["player_1", "player_2", "player_3", "player_4", "player_5", "bdht_1", "win_1"]
    team2keys = ["player_6", "player_7", "player_8", "player_9", "player_10", "bdht_2", "win_2"]
    keys =["matchId", "gameVersion", "player_lane", *team1keys, *team2keys]
    df = pd.DataFrame(columns=keys)

    for match in matchlist:
        url4overall = "https://asia.api.riotgames.com/lol/match/v5/matches/" + match
        call = requests.get(url4overall, headers=headers)
        while call.status_code != 200:
            print(f"Status code: {call.status_code}")
            if call.status_code == 429:
                print("Too busy. Wait 2 mins.")
                time.sleep(120)
            elif call.status_code == 500:
                print("API key is out of dated.")
                return
            time.sleep(2)
        overall = call.json()

        matchId = overall['metadata']['matchId']
        gameVersion = overall['info']['gameVersion']
        # playerData
        for j in range(10):
            position = overall['info']['participants'][j]['summonerName']
            if position == summonerName:
                player_position = j+1
            championName = overall['info']['participants'][j]['championName']
            lane = overall['info']['participants'][j]['individualPosition']
            kills = overall['info']['participants'][j]['kills']
            deaths = overall['info']['participants'][j]['deaths']
            assists = overall['info']['participants'][j]['assists']
            cs = overall['info']['participants'][j]['totalMinionsKilled'] + overall['info']['participants'][j]['neutralMinionsKilled']

            if overall['info']['participants'][j]['teamId'] == 100:
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
            elif overall['info']['participants'][j]['teamId'] == 200:
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
            baron = overall['info']['teams'][j]['objectives']['baron']['kills']
            dragon = overall['info']['teams'][j]['objectives']['dragon']['kills']
            herald = overall['info']['teams'][j]['objectives']['riftHerald']['kills']
            tower = overall['info']['teams'][j]['objectives']['tower']['kills']
            win = overall['info']['teams'][j]['win']

            if overall['info']['teams'][j]['teamId'] == 100:
                object_1 = f"{baron}, {dragon}, {herald}, {tower}"
                win_1 = f"{win}"
            else:
                object_2 = f"{baron}, {dragon}, {herald}, {tower}"
                win_2 = f"{win}"

        values = [matchId, gameVersion, player_position, player_1, player_2, player_3, player_4, player_5, object_1, win_1, player_6, player_7, player_8, player_9, player_10, object_2, win_2]
        idx = len(df)
        df.loc[idx] = values
    return df

def dataset_for_me_v2(df, champion, lane=None, tier=None):
    tier_df = df

    matchId_df = tier_df.iloc[:, 0]
    tier = tier_df['player_lane']
    team1_df = tier_df.iloc[:, 3:10]
    team1_df = pd.concat([matchId_df, tier, team1_df], axis=1)
    team2_df = tier_df.iloc[:, 10:17]
    team2_df = pd.concat([matchId_df, tier, team2_df], axis=1)
    team2_df.rename(columns={
            "matchId": "matchId",
            "rank": "rank",
            "player_6": "player_1",
            "player_7": "player_2",
            "player_8": "player_3",
            "player_9": "player_4",
            "player_10": "player_5",
            "bdht_2": "bdht_1",
            "win_2": "win_1"
    }, inplace=True)
    fn_df = pd.concat([team1_df, team2_df], axis=0, ignore_index=True)
    dataset = pd.DataFrame(columns=[
            'matchId', 'rank', 'lane', 'kills', 'deaths', 'assists', 'cs', 'barons', 'dragons', 'heralds', 'towers', 'total_kills', 'total_deaths', 'win'
        ])
    for i in range(len(fn_df)):
        matchId = fn_df.iloc[i, 0]
        tier = fn_df.iloc[i, 1]
        team_df = fn_df.iloc[i, 7].split(',')
        team_total_kills = 0
        team_total_deaths = 0
        for k in range(5):
            champ_df = fn_df.iloc[i, k+2].split(',')
            team_total_kills += int(champ_df[2])
            team_total_deaths += int(champ_df[3])
        for j in range(5):
            champ_df = fn_df.iloc[i, j+2].split(',')
            if champ_df[0] == champion:
                if lane == None:
                    position = champ_df[1].strip()      # str
                else:
                    if lane == champ_df[1].strip():
                        position = champ_df[1].strip()      # str
                    else:
                        continue
                kills = champ_df[2]         # int
                deaths = champ_df[3]        # int
                assists = champ_df[4]       # int
                cs = champ_df[5]            # int
                barons = team_df[0]         # int
                dragons = team_df[1]        # int
                heralds = team_df[2]        # int
                towers = team_df[3]         # int
                win = fn_df.iloc[i, 8]      # bool
                dataset.loc[len(dataset)] = [matchId, tier, position, kills, deaths, 
                                            assists, cs, barons, dragons, heralds, 
                                            towers, team_total_kills, team_total_deaths, win]
    return dataset

def dataset_for_me(df, champion, lane=None, tier=None):
    tier_df = df

    matchId_df = tier_df.iloc[:, 0]
    tier = tier_df['player_lane']
    team1_df = tier_df.iloc[:, 3:10]
    team1_df = pd.concat([matchId_df, tier, team1_df], axis=1)
    team2_df = tier_df.iloc[:, 10:17]
    team2_df = pd.concat([matchId_df, tier, team2_df], axis=1)
    team2_df.rename(columns={
            "matchId": "matchId",
            "rank": "rank",
            "player_6": "player_1",
            "player_7": "player_2",
            "player_8": "player_3",
            "player_9": "player_4",
            "player_10": "player_5",
            "bdht_2": "bdht_1",
            "win_2": "win_1"
    }, inplace=True)
    fn_df = pd.concat([team1_df, team2_df], axis=0, ignore_index=True)
    dataset = pd.DataFrame(columns=[
            'matchId', 'rank', 'lane', 'kills', 'deaths', 'assists', 'cs', 'barons', 'dragons', 'heralds', 'towers', 'win'
        ])
    for i in range(len(fn_df)):
        matchId = fn_df.iloc[i, 0]
        tier = fn_df.iloc[i, 1]
        team_df = fn_df.iloc[i, 7].split(',')

        for j in range(5):
            champ_df = fn_df.iloc[i, j+2].split(',')
            if champ_df[0] == champion:
                if lane == None:
                    position = champ_df[1].strip()      # str
                else:
                    if lane == champ_df[1].strip():
                        position = champ_df[1].strip()      # str
                    else:
                        continue
                kills = champ_df[2]         # int
                deaths = champ_df[3]        # int
                assists = champ_df[4]       # int
                cs = champ_df[5]            # int
                barons = team_df[0]         # int
                dragons = team_df[1]        # int
                heralds = team_df[2]        # int
                towers = team_df[3]         # int
                win = fn_df.iloc[i, 8]      # bool
                dataset.loc[len(dataset)] = [matchId, tier, position, kills, deaths, 
                                            assists, cs, barons, dragons, heralds, 
                                            towers, win]
    return dataset


if __name__ == "__main__":
    puuid = getPuuid("고츄장떡")
    tier = getTier("고츄장떡")
    matchlist = getMatchlist(puuid)
    df = getData("고츄장떡", matchlist)
    mydf = dataset_for_me_v2(df, "Lux")
    mydf_html = mydf.to_html()
    print(mydf)
    