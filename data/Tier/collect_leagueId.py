import requests
import json
import os, time, pickle

# tier; league v4
api_key = "RGAPI-7543d971-dbf7-4eeb-8972-395b77b2f019"

request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }

# Create directory
def create_dir(tier, division):
    if os.path.exists(f'data/Tier/{tier}/{division}') == False:
        if os.path.exists(f'data/Tier/{tier}') == False:
            os.mkdir(f'data/Tier/{tier}')
        os.mkdir(f'data/Tier/{tier}/{division}')


# Collect matchId sample
def collect_tier(api_key, tier, division, page=100):
    ## requests 낭비의 문제로 Riot API에서 차단당할 수 있다.
    ## 100명 * 최대 20게임 = 최대 2000게임 호출
    ## 2000판 호출되는데 한 판 당 3번의 조회가 필요...
    ## 한 티어를 호출하는데만 최대 6000 requests가 필요하다.
    ## 따라서 미운털 안 박히려면 처신 잘 해야될 것이다.
    if tier == "DIAMOND":
        if division == "I":
            page = 40
        elif division == "II":
            page = 60
        elif division == "III":
            page = 80
    
    while 1:
        tier_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}?page={page}"

        '''
        tier: ["DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "IRON"]
        division: ["I", "II", "III", "IV"]

        If you select number that are bigger than {page}, {tier_js} will not be show.
        '''
        tier_r = requests.get(tier_url, headers=request_header)

        if tier_r.status_code == 200:
            tier_js = tier_r.json()
            if len(tier_js) == 0:
                page -= 1
                continue
            elif len(tier_js) > 0:
                break
        elif tier_r.status_code != 200:
            print(f"[Error] {tier_r.status_code}")
            time.sleep(5)

    # print(len(tier_js))
    
    print(f"{tier} {division} usernames acquired... Wait a second for making matchId list.")    
    time.sleep(10)

    matchId_list = []

    # Tier 변동이 실시간으로 일어나기 떄문에 해당 tier 하위 20%을 추려냄. 저티어 구간일수록 변동인원이 많음을 고려.
    i = 0
    while i <= int(len(tier_js)*0.8):
        try:
            summonerName = tier_js[i]['summonerName']
        
            puuid_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + api_key
            puuid_r = requests.get(puuid_url, headers=request_header)
            puuid = puuid_r.json()['puuid']
            if puuid_r.status_code != 200:
                raise Exception

            matchId_url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids" + "?api_key=" + api_key + "&type=ranked&start=0&count=20"
            matchId_r = requests.get(matchId_url, headers=request_header)
            if matchId_r.status_code != 200:
                raise Exception

            matchId_js = matchId_r.json()
            matchId_list.append(matchId_js)
            i += 1
            print(f"{i} / {int(len(tier_js)*0.8+1)} USERS")
        except Exception:
            print(f"[Error] {puuid_r.status_code}")
            if puuid_r.status_code == 429:
                time.sleep(120)
            elif puuid_r.status_code == 404:
                i += 1

    matchId_list = [elem for array in matchId_list for elem in array]
    print(f"Total match: {len(matchId_list)+1}")

    matchId_list = list(set(matchId_list))
    print(f"Collected match: {len(matchId_list)+1}")

    matchId_dict = {
            'tier': tier,
            'division': division,
            'matchId': matchId_list,
            }
    
    # Save .pkl
    create_dir(tier, division)
    with open(f'data/Tier/{tier}/{division}/{tier}_{division}.pkl', 'wb') as f:
        pickle.dump(matchId_dict, f)
    
    print(f"{tier} {division} samples are saved!!\ndir: {os.getcwd()}/Tier/{tier}/{division}/{tier}_{division}.pkl\n")
    # return matchId_dict





# DIAMOND sample
# collect_tier(api_key, "DIAMOND", "I")
# collect_tier(api_key, "DIAMOND", "II")
# collect_tier(api_key, "DIAMOND", "III")
# collect_tier(api_key, "DIAMOND", "IV")

# # PLATINUM sample
# collect_tier(api_key, "PLATINUM", "I")
# collect_tier(api_key, "PLATINUM", "II")
# collect_tier(api_key, "PLATINUM", "III")
# collect_tier(api_key, "PLATINUM", "IV")

# # GOLD sample
# collect_tier(api_key, "GOLD", "I")
# collect_tier(api_key, "GOLD", "II")
# collect_tier(api_key, "GOLD", "III")
# collect_tier(api_key, "GOLD", "IV")

# # SILVER sample
# collect_tier(api_key, "SILVER", "I")
# collect_tier(api_key, "SILVER", "II")
# collect_tier(api_key, "SILVER", "III")
# collect_tier(api_key, "SILVER", "IV")

# # BRONZE sample
# collect_tier(api_key, "BRONZE", "I")
# collect_tier(api_key, "BRONZE", "II")
# collect_tier(api_key, "BRONZE", "III")
# collect_tier(api_key, "BRONZE", "IV")