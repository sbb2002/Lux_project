import pickle
import requests
import os, json, time, logging, datetime
from glob import glob

api_key = "RGAPI-c05799b8-e0a5-477b-a1e4-6a8e142636f3"

request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }

# logging
logging.basicConfig(
    format='[%(levelname)s] %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger()
file_handler = logging.FileHandler(f'data/Tier/report.log')
logger.addHandler(file_handler)

# # DIAMOND
# with open('data/Tier/DIAMOND/I/DIAMOND_I.pkl', 'rb') as f:
#     D1 = pickle.load(f)
# with open('data/Tier/DIAMOND/II/DIAMOND_II.pkl', 'rb') as f:
#     D2 = pickle.load(f)
# with open('data/Tier/DIAMOND/III/DIAMOND_III.pkl', 'rb') as f:
#     D3 = pickle.load(f)
# with open('data/Tier/DIAMOND/IV/DIAMOND_IV.pkl', 'rb') as f:
#     D4 = pickle.load(f)

# # PLATINUM
# with open('data/Tier/PLATINUM/I/PLATINUM_I.pkl', 'rb') as f:
#     P1 = pickle.load(f)
# with open('data/Tier/PLATINUM/II/PLATINUM_II.pkl', 'rb') as f:
#     P2 = pickle.load(f)
# with open('data/Tier/PLATINUM/III/PLATINUM_III.pkl', 'rb') as f:
#     P3 = pickle.load(f)
# with open('data/Tier/PLATINUM/IV/PLATINUM_IV.pkl', 'rb') as f:
#     P4 = pickle.load(f)

# # GOLD
# with open('data/Tier/GOLD/I/GOLD_I.pkl', 'rb') as f:
#     G1 = pickle.load(f)
# with open('data/Tier/GOLD/II/GOLD_II.pkl', 'rb') as f:
#     G2 = pickle.load(f)
# with open('data/Tier/GOLD/III/GOLD_III.pkl', 'rb') as f:
#     G3 = pickle.load(f)
# with open('data/Tier/GOLD/IV/GOLD_IV.pkl', 'rb') as f:
#     G4 = pickle.load(f)

# # SILVER
# with open('data/Tier/SILVER/I/SILVER_I.pkl', 'rb') as f:
#     S1 = pickle.load(f)
# with open('data/Tier/SILVER/II/SILVER_II.pkl', 'rb') as f:
#     S2 = pickle.load(f)
# with open('data/Tier/SILVER/III/SILVER_III.pkl', 'rb') as f:
#     S3 = pickle.load(f)
# with open('data/Tier/SILVER/IV/SILVER_IV.pkl', 'rb') as f:
#     S4 = pickle.load(f)

# BRONZE
# with open('data/Tier/BRONZE/I/BRONZE_I.pkl', 'rb') as f:
#     B1 = pickle.load(f)
# with open('data/Tier/BRONZE/II/BRONZE_II.pkl', 'rb') as f:
#     B2 = pickle.load(f)
with open('data/Tier/BRONZE/III/BRONZE_III.pkl', 'rb') as f:
    B3 = pickle.load(f)
with open('data/Tier/BRONZE/IV/BRONZE_IV.pkl', 'rb') as f:
    B4 = pickle.load(f)


def get_data(dict_match):
    # params
    tier = dict_match['tier']
    division = dict_match['division']
    matchId = dict_match['matchId']
    number = len(dict_match['matchId'])

    # continue
    existFileCount = len(glob(f'data/Tier/{tier}/{division}/overall/*.json'))

    # mkdir
    if os.path.exists(f'data/Tier/{tier}/{division}/overall') == False:
        os.mkdir(f'data/Tier/{tier}/{division}/overall')
        print("[overall] directory is created.")
    if os.path.exists(f'data/Tier/{tier}/{division}/timeline') == False:
        os.mkdir(f'data/Tier/{tier}/{division}/timeline')
        print("[timeline] directory is created.")

    logger.info(f'[{datetime.datetime.now()}] Start: {tier}-{division}')
    print(f"***************************************************\nData acquiring is starting.\nTier:\t{tier} {division}\nTotal:\t{number}\n\nProgress:")

    i = 0       # number for while
    if existFileCount != 0:
        i = existFileCount - 1
        logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number} Continue.')
    retry_token = 3     # Retry-able code confrontation

    while i < number:
        try:
            # call data
            overall = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId[i]}"
            timeline = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId[i]}/timeline"
            overall_r = requests.get(overall, headers=request_header)
            timeline_r = requests.get(timeline, headers=request_header)

            if overall_r.status_code != 200 or timeline_r.status_code != 200:
                raise Exception 

            # save data
            with open(f'data/Tier/{tier}/{division}/overall/{matchId[i]}.json', 'w') as f:
                json.dump(overall_r.json(), f, indent=4, ensure_ascii=False)
            with open(f'data/Tier/{tier}/{division}/timeline/{matchId[i]}_timeline.json', 'w') as f:
                json.dump(timeline_r.json(), f, indent=4, ensure_ascii=False)
            
            print(f"{i+1} / {number}")
            i += 1
            retry_token = 3

        except Exception:
            # response check
            # 4XX;  400=bad request, 401=unauthorized, 403=forbidden, 404=not found, 415=unsupported media type, 429=rate limit exceeded
            # 5XX;  500=internal error, 503=service unavailable
            if overall_r.status_code == 429 or timeline_r == 429:
                logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.429\tToo busy')
                time.sleep(120)
                continue

            elif overall_r.status_code == 404 or timeline_r == 404:
                logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.404\tNot found')
                i += 1
                continue

            elif overall_r.status_code == 503 or timeline_r == 503:
                logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.503\tService unavailable. But continue. Retry: {retry_token}')
                retry_token -= 1
                if retry_token == 0:
                    logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.503\tService unavailable. Pass! Retry: {retry_token}')
                    i += 1
                    retry_token = 3
                    continue

            else:
                if overall_r.status_code == 200 or timeline_r == 200:
                    logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.200\tUnknown error. But continue. Retry: {retry_token}')
                    retry_token -= 1
                    if retry_token == 0:
                        logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.200\tUnknown error. Pass! Retry: {retry_token}')
                        i += 1
                        retry_token = 3
                        continue
                else:
                    logger.info(f'[{datetime.datetime.now()}] {tier}-{division}\t{i+1}/{number}\tErrno.{overall_r.status_code}\tCritical error. Break!')
                    break
    time.sleep(3)

    recFileCount = len(glob(f'data/Tier/{tier}/{division}/overall/*.json'))
    logger.info(f'[{datetime.datetime.now()}] End: {tier}-{division}\t{recFileCount} matches are written successfully.')


#################################################################
tier = [B3, B4]        # G1 log


for i in range(2):
    get_data(tier[i])


print("All progress are finished!! Shutdown after 20sec.")
os.system("shutdown -s -t 20")




# print("\nDIAMOND tier match")
# print(len(D1['matchId']))
# print(len(D2['matchId']))
# print(len(D3['matchId']))
# print(len(D4['matchId']))
# D_sum = len(D1['matchId'])+len(D2['matchId'])+len(D3['matchId'])+len(D4['matchId'])
# print(f"SUM:\t{D_sum}")

# print("\nPLATINUM tier match")
# print(len(P1['matchId']))
# print(len(P2['matchId']))
# print(len(P3['matchId']))
# print(len(P4['matchId']))
# P_sum = len(P1['matchId'])+len(P2['matchId'])+len(P3['matchId'])+len(P4['matchId'])
# print(f"SUM:\t{P_sum}")

# print("\nGOLD tier match")
# print(len(G1['matchId']))
# print(len(G2['matchId']))
# print(len(G3['matchId']))
# print(len(G4['matchId']))
# G_sum = len(G1['matchId'])+len(G2['matchId'])+len(D3['matchId'])+len(D4['matchId'])
# print(f"SUM:\t{G_sum}")

# print("\nSILVER tier match")
# print(len(S1['matchId']))
# print(len(S2['matchId']))
# print(len(S3['matchId']))
# print(len(S4['matchId']))
# S_sum = len(S1['matchId'])+len(S2['matchId'])+len(S3['matchId'])+len(S4['matchId'])
# print(f"SUM:\t{S_sum}")

# print("\nBRONZE tier match")
# print(len(B1['matchId']))
# print(len(B2['matchId']))
# print(len(B3['matchId']))
# print(len(B4['matchId']))
# B_sum = len(B1['matchId'])+len(B2['matchId'])+len(B3['matchId'])+len(B4['matchId'])
# print(f"SUM:\t{B_sum}")

# print(f"\n################################################\nTotal:\t{D_sum+P_sum+G_sum+S_sum+B_sum}")

