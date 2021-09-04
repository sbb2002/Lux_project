import json

with open(r'data\Tier\DIAMOND\I\timeline\KR_5266752731_timeline.json', 'r', encoding='cp949') as f:
    a = json.load(f)

metadata = a['metadata']
info = a['info']

# print(metadata.keys())  # dataVersion, matchId, participants(puuid)
print(info.keys())

frameInterval = info['frameInterval']   # 60000
frames = info['frames']     # dataList; dict_keys(['events', 'participantFrames', 'timestamp']) / 18 sections
gameId = info['gameId']     # 5266752731
participants = info['participants']     # participantsId(1~10), puuid

print(frames[2]['events'][11].keys())





'''
# print(metadata.keys())
type: dict
dataVersion, matchId, participants(puuid)

# print(frames[0]['events'])
type: list(1) > dict
[{'realTimestamp': 1623877354850, 'timestamp': 0, 'type': 'PAUSE_END'}]
Simple time stamp


## print(frames[1]['events'])
type: list(34) > dict
Situation in same time

### print(frames[1]['events'][0])
type: dict
{'itemId': 1035, 'participantId': 7, 'timestamp': 3834, 'type': 'ITEM_PURCHASED'}

### print(frames[2]['events'][11].keys())
type: dict
dict_keys([
    'assistingParticipantIds', 'bounty', 'killStreakLength', 'killerId', 
    'position', 'timestamp', 'type', 'victimDamageDealt', 'victimDamageReceived', 
    'victimId'
    ])

==============================================================================
print(frames[timeFrame]['events'][detailTimeStamp]['type'])
type: str
ITEM_PURCHASED, SKILL_LEVEL_UP, WARD_KILL, WARD_PLACED, CHAMPION_KILL, ...
==============================================================================


# print(frames[0]['participantFrames'].keys())
type: dict > dict (> ...)
dict_keys(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
in-game stats, dict

## print(frames[0]['participantFrames']['1'].keys()); in-game stats
type: dict
dict_keys([
        'championStats', 'currentGold', 'damageStats', 'goldPerSecond', 
        'jungleMinionsKilled', 'level', 'minionsKilled', 'participantId', 
        'position', 'timeEnemySpentControlled', 'totalGold', 'xp'
        ])


# print(frames[0]['timestamp'])
0 (ms)
'''