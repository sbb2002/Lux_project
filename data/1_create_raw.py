import requests
import json
import os, time
  
# params
summoner_id = "고츄장떡"
api_key = 'RGAPI-8eeadb19-8b00-4e20-bc8d-8961a400f8ff'

# api url
api_url = "https://kr.api.riotgames.com"
api_asia_url = "https://asia.api.riotgames.com"

# get id
summoner_url = api_url + "/lol/summoner/v4/summoners/by-name/" + summoner_id + "?api_key=" + api_key
summoner_r = requests.get(summoner_url)

# get puuid
league_url = api_url + "/lol/league/v4/entries/by-summoner/" + summoner_r.json()['id'] + "?api_key=" + api_key
league_r = requests.get(league_url)

# get matchid
match_url = api_asia_url + "/lol/match/v5/matches/by-puuid/" + summoner_r.json()['puuid'] + "/ids" + "?api_key=" + api_key + "&type=ranked&start=0&count=24"
match_r = requests.get(match_url)

print(match_r.json())
print("It takes a few seconds......\n")

# get match data overall and timeline
count = 0
for i in range(len(match_r.json())):
    overall_url = api_asia_url + "/lol/match/v5/matches/" + match_r.json()[i] + "?api_key=" + api_key
    overall_r = requests.get(overall_url)
    timeline_url = api_asia_url + "/lol/match/v5/matches/" + match_r.json()[i] + "/timeline" + "?api_key=" + api_key
    timeline_r = requests.get(timeline_url)
    gamemode = overall_r.json().get('info').get('gameMode')
    if os.path.exists(f'./data/gameMode/{gamemode}') == False:
        os.mkdir(f'./data/gameMode/{gamemode}')
        os.mkdir(f'./data/gameMode/{gamemode}/overall')
        os.mkdir(f'./data/gameMode/{gamemode}/timeline')
    with open(f'./data/gameMode/{gamemode}/overall/{match_r.json()[i]}.json', "w") as f:
        json.dump(overall_r.json(), f, indent=4, ensure_ascii=False)    
    with open(f'./data/gameMode/{gamemode}/timeline/{match_r.json()[i]}_timeline.json', "w") as f:
        json.dump(timeline_r.json(), f, indent=4, ensure_ascii=False)
    time.sleep(1)
    count += 1
    print(f"{match_r.json()[i]} data were updated.")

# report
print(f"{count} files added.")
print("Data saving is finished!!!\n")