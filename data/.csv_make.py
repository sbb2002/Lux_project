import csv
import os
import re
import json

p = re.compile('[a-zA-Z]+')

filelist = os.listdir('data/overall')

def make_csv(filename):
    with open(f'data/csv/{filename}.csv', 'w', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(match['info']['participants'][0].keys())
        for player in range(10):
            w.writerow(match['info']['participants'][player].values())

    print(f"{filename}.csv was written successfully.")

def make_readme(match):
    with open('data/csv/readme.md', 'w') as f:
        info = match['info']['participants'][0]
        infoTypes =  [type(v) for v in info.values()]
        infoKeys = [k for k in info.keys()]
        for num in range(len(info)):
            line = str(num) + "\t" + str(infoTypes[num]) + "\t" + str(infoKeys[num]) + "\n"
            f.write(line)

def row_like(filename, whoRU):
    '''
    To do...
    1. input()을 써서 내 정보가 우선적으로 앞에 오고 나머지 플레이어의 스텟을 나열할 것.
    2. json 76th "summonerName"이 unicode로 적혀있다. euc-kr일 때는 한글로 적혀져 있었는데...
      이것때문에 puuid를 활용하던, euc-kr로 해봐야겠따.
    '''
    with open(f'data/csv/{filename}.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        match_data = [line for line in rdr]
        print(match_data[1][76])
        del match_data[0]
        match_list = []
        match_list.append(f'{filename}')
        match_list.extend(match_data)
        # matchId, Players_stats x 10

    with open(f'data/match_record.csv', 'a+', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(match_list)
        # print(f"{filename} record was written.")


################################################################
if os.path.exists('data/match_record.csv') == True:
    os.remove('data/match_record.csv')

whoRU = input("What is your summoner name?")

with open(f'data/overall/{filename}.json', 'r', encoding='utf-8') as f:
    match = json.load(f)

for i in range(len(filelist)):
    filename = os.path.splitext(filelist[i])
    filename = filename[0]
    
    row_like(filename, whoRU)

#     with open(f'data/overall/{filename}.json', 'r') as f:
#         match = json.load(f)

    make_csv(filename)
make_readme(match)

# print("Making .csv is finished!!")