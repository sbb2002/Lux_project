import json

with open("data/timeline/KR_5138516254_timeline.json", 'r') as f:
    match = json.load(f)

print(match.keys())
print(match['metadata'].keys())
print(match['info'].keys())

print("\nframes are ...")
print(len(match['info']['frames']))
print(type(match['info']['frames']))

# print("########################################################")

# print("\nFirst frame contains ...")
# print(len(match['info']['frames'][0]))
# print(type(match['info']['frames'][0]))
# print(match['info']['frames'][0].keys())

# print("\n\t1. events \n")
# print(match['info']['frames'][0]['events'])
# print(type(match['info']['frames'][0]['events']))

# print("\n\t2. participantFrames \n")
# # print(match['info']['frames'][0]['participantFrames'].keys())
# print(type(match['info']['frames'][0]['participantFrames']))
# print(len(match['info']['frames'][0]['participantFrames']))

# print("\n\t3. timestamp \n")
# print(match['info']['frames'][0]['timestamp'])
# print(type(match['info']['frames'][0]['timestamp']))

print("########################################################")

for i in range(len(match['info']['frames'])):
    print(f"{i} - frame: ")
    print(len(match['info']['frames'][i]))
    print(type(match['info']['frames'][i]))
    print(match['info']['frames'][i].keys())
    print("\n...........................................\n")

print("########################################################")

print("Structure Info.: ")

print("events: ")
print(match['info']['frames'][0]['events'])

print("\n...........................................\n")


print("participantFrames: ")
print(match['info']['frames'][0]['participantFrames'].keys())

print("\n...........................................\n")

print("participantFrames - 1: ")
print(match['info']['frames'][0]['participantFrames']['1'].keys())
print(len(match['info']['frames'][0]['participantFrames']['1'].keys()))

print("\n...........................................\n")

print("participantFrames - 1 - championStats: ")
print(match['info']['frames'][0]['participantFrames']['1']['championStats'].keys())
print(len(match['info']['frames'][0]['participantFrames']['1']['championStats'].keys()))

print("\n...........................................\n")

print("participantFrames - 1 - championStats - abilltyPower: ")
print(match['info']['frames'][0]['participantFrames']['1']['championStats']['abilityPower'])

print("\n...........................................\n")

print("participantFrames - 1 - championStats - abilltyPower: ")
print(match['info']['frames'][0]['participantFrames']['1']['championStats']['abilityPower'])


print("\n...........................................\n")
print("\n...........................................\n")

print("timestamp: ")
print(match['info']['frames'][0]['timestamp'])