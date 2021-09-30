import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv(r'D:\\PythonWorkspace\\gitrepo\\data_by_rank_v2.csv', sep=',')

def dataset(champion, lane=None, tier=None):
    global df

    if tier != None:
        if type(tier) is list:
            n = 0
            for i in range(len(tier)):
                isTier = (df['rank'] == tier[i])
                if n == 0:
                    tier_df = df[isTier]
                    n += 1
                else:
                    tier_df = pd.concat([tier_df, df[isTier]], axis=0, ignore_index=True)
        else:
            isTier = (df['rank'] == tier)
            tier_df = df[isTier]
    else:
        tier_df = df
    
    tier = tier_df['rank']
    team1_df = tier_df.iloc[:, 3:10]
    team1_df = pd.concat([tier, team1_df], axis=1)
    team2_df = tier_df.iloc[:, 10:17]
    team2_df = pd.concat([tier, team2_df], axis=1)


    team2_df.rename(columns={
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
            'rank', 'lane', 'kills', 'deaths', 'assists', 'cs', 'barons', 'dragons', 'heralds', 'towers', 'win'
        ])

    for i in range(len(fn_df)):
        tier = fn_df.iloc[i, 0]
        team_df = fn_df.iloc[i, 6].split(',')

        for j in range(5):
            champ_df = fn_df.iloc[i, j+1].split(',')

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
                win = fn_df.iloc[i, 7]      # bool

                dataset.loc[len(dataset)] = [tier, position, kills, deaths, assists, cs, barons, dragons, heralds, towers, win]
    
    return dataset

def dataset_v2(champion, lane=None, tier=None):
    global df

    if tier != None:
        if type(tier) is list:
            n = 0
            for i in range(len(tier)):
                isTier = (df['rank'] == tier[i])
                if n == 0:
                    tier_df = df[isTier]
                    n += 1
                else:
                    tier_df = pd.concat([tier_df, df[isTier]], axis=0, ignore_index=True)
        else:
            isTier = (df['rank'] == tier)
            tier_df = df[isTier]
    else:
        tier_df = df
    
    tier = tier_df['rank']
    team1_df = tier_df.iloc[:, 3:10]
    team1_df = pd.concat([tier, team1_df], axis=1)
    team2_df = tier_df.iloc[:, 10:17]
    team2_df = pd.concat([tier, team2_df], axis=1)


    team2_df.rename(columns={
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
            'rank', 'lane', 'kills', 'deaths', 'assists', 'cs', 'barons', 'dragons', 'heralds', 'towers', 'total_kills', 'total_deaths', 'win'
        ])

    for i in range(len(fn_df)):
        tier = fn_df.iloc[i, 0]
        team_df = fn_df.iloc[i, 6].split(',')
        team_total_kills = 0
        team_total_deaths = 0

        for k in range(5):
            champ_df = fn_df.iloc[i, k+1].split(',')
            team_total_kills += int(champ_df[2])
            team_total_deaths += int(champ_df[3])

        for j in range(5):
            champ_df = fn_df.iloc[i, j+1].split(',')

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
                win = fn_df.iloc[i, 7]      # bool

                dataset.loc[len(dataset)] = [tier, position, kills, deaths, assists, cs, barons, dragons, heralds, towers, team_total_kills, team_total_deaths, win]
    
    return dataset


def tt_split(dataset):
    X_train, X_test, y_train, y_test = \
        train_test_split(dataset.iloc[:, 2:-1], dataset.iloc[:, -1], train_size=0.8, random_state=42, stratify=dataset.iloc[:, [-1]], shuffle=True)
    y_train = y_train.astype('bool')
    y_test = y_test.astype('bool')
    mm_scaler = MinMaxScaler()
    mm_scaler.fit(X_train)
    X_train_scaled = mm_scaler.transform(X_train)
    X_test_scaled = mm_scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test

