import json
from pprint import pprint as pp
import csv

with open('data/overall/KR_5138516254.json', 'r') as f:
    match = json.load(f)

print(match.keys())

print(match['info'].keys())

# print(len(match['info']['participants']))       # 참가인원 10명의 통계기록 뭉탱이
# print(len(match['info']['participants'][0]))       # 1번 유저 - 102개의 keys

# dict stacking
with open('./data/csv/KR_5138516254.csv', 'w', encoding='euc-kr') as f:
    write = csv.writer(f)
    write.writerow(match['info']['participants'][0].keys())
    for player in range(10):
        write.writerow(match['info']['participants'][player].values())
