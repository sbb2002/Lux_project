import requests
import json
import pandas as pd
import os, time
  
# params
summoner_id = "고츄장떡"
api_key = 'RGAPI-0ca59a18-e5b7-4470-b65e-59bb8feda125'

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
match_url = api_asia_url + "/lol/match/v5/matches/by-puuid/" + summoner_r.json()['puuid'] + "/ids" + "?api_key=" + api_key + "&start=0&count=24"
match_r = requests.get(match_url)

print("It takes a few seconds......\n")

# get match data overall and timeline
for i in range(len(match_r.json())):
    overall_url = api_asia_url + "/lol/match/v5/matches/" + match_r.json()[i] + "?api_key=" + api_key
    overall_r = requests.get(overall_url)
    with open(f'./data/overall/{match_r.json()[i]}.json', "w") as f:
        json.dump(overall_r.json(), f, indent=4)
    timeline_url = api_asia_url + "/lol/match/v5/matches/" + match_r.json()[i] + "/timeline" + "?api_key=" + api_key
    timeline_r = requests.get(timeline_url)
    with open(f'./data/timeline/{match_r.json()[i]}_timeline.json', "w") as f:
        json.dump(timeline_r.json(), f, indent=4)
    time.sleep(1)

# report
print(f"{len(match_r.json())} data were updated.")
print(f"There are {len(os.listdir('data/overall'))} files.")
print("Data saving is finished!!!\n")