import pickle

# DIAMOND
with open('data/Tier/DIAMOND/I/DIAMOND_I.pkl', 'rb') as f:
    D1 = pickle.load(f)
with open('data/Tier/DIAMOND/II/DIAMOND_II.pkl', 'rb') as f:
    D2 = pickle.load(f)
with open('data/Tier/DIAMOND/III/DIAMOND_III.pkl', 'rb') as f:
    D3 = pickle.load(f)
with open('data/Tier/DIAMOND/IV/DIAMOND_IV.pkl', 'rb') as f:
    D4 = pickle.load(f)

# PLATINUM
with open('data/Tier/PLATINUM/I/PLATINUM_I.pkl', 'rb') as f:
    P1 = pickle.load(f)
with open('data/Tier/PLATINUM/II/PLATINUM_II.pkl', 'rb') as f:
    P2 = pickle.load(f)
with open('data/Tier/PLATINUM/III/PLATINUM_III.pkl', 'rb') as f:
    P3 = pickle.load(f)
with open('data/Tier/PLATINUM/IV/PLATINUM_IV.pkl', 'rb') as f:
    P4 = pickle.load(f)

# GOLD
with open('data/Tier/GOLD/I/GOLD_I.pkl', 'rb') as f:
    G1 = pickle.load(f)
with open('data/Tier/GOLD/II/GOLD_II.pkl', 'rb') as f:
    G2 = pickle.load(f)
with open('data/Tier/GOLD/III/GOLD_III.pkl', 'rb') as f:
    G3 = pickle.load(f)
with open('data/Tier/GOLD/IV/GOLD_IV.pkl', 'rb') as f:
    G4 = pickle.load(f)

# SILVER
with open('data/Tier/SILVER/I/SILVER_I.pkl', 'rb') as f:
    S1 = pickle.load(f)
with open('data/Tier/SILVER/II/SILVER_II.pkl', 'rb') as f:
    S2 = pickle.load(f)
with open('data/Tier/SILVER/III/SILVER_III.pkl', 'rb') as f:
    S3 = pickle.load(f)
with open('data/Tier/SILVER/IV/SILVER_IV.pkl', 'rb') as f:
    S4 = pickle.load(f)

# BRONZE
with open('data/Tier/BRONZE/I/BRONZE_I.pkl', 'rb') as f:
    B1 = pickle.load(f)
with open('data/Tier/BRONZE/II/BRONZE_II.pkl', 'rb') as f:
    B2 = pickle.load(f)
with open('data/Tier/BRONZE/III/BRONZE_III.pkl', 'rb') as f:
    B3 = pickle.load(f)
with open('data/Tier/BRONZE/IV/BRONZE_IV.pkl', 'rb') as f:
    B4 = pickle.load(f)

print("\nDIAMOND tier match")
print(len(D1['matchId']))
print(len(D2['matchId']))
print(len(D3['matchId']))
print(len(D4['matchId']))
D_sum = len(D1['matchId'])+len(D2['matchId'])+len(D3['matchId'])+len(D4['matchId'])
print(f"SUM:\t{D_sum}")

print("\nPLATINUM tier match")
print(len(P1['matchId']))
print(len(P2['matchId']))
print(len(P3['matchId']))
print(len(P4['matchId']))
P_sum = len(P1['matchId'])+len(P2['matchId'])+len(P3['matchId'])+len(P4['matchId'])
print(f"SUM:\t{P_sum}")

print("\nGOLD tier match")
print(len(G1['matchId']))
print(len(G2['matchId']))
print(len(G3['matchId']))
print(len(G4['matchId']))
G_sum = len(G1['matchId'])+len(G2['matchId'])+len(D3['matchId'])+len(D4['matchId'])
print(f"SUM:\t{G_sum}")

print("\nSILVER tier match")
print(len(S1['matchId']))
print(len(S2['matchId']))
print(len(S3['matchId']))
print(len(S4['matchId']))
S_sum = len(S1['matchId'])+len(S2['matchId'])+len(S3['matchId'])+len(S4['matchId'])
print(f"SUM:\t{S_sum}")

print("\nBRONZE tier match")
print(len(B1['matchId']))
print(len(B2['matchId']))
print(len(B3['matchId']))
print(len(B4['matchId']))
B_sum = len(B1['matchId'])+len(B2['matchId'])+len(B3['matchId'])+len(B4['matchId'])
print(f"SUM:\t{B_sum}")

print(f"\n################################################\nTotal:\t{D_sum+P_sum+G_sum+S_sum+B_sum}")