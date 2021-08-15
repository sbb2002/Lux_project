import pandas as pd
import numpy as np

df = pd.read_csv('data/csv/KR_5138516254.csv', encoding='utf-8', delimiter=',')

# print(df.head(10))
# print(df.shape)
# print("individualPosittion: \n", df.iloc[:,25])
# print("teamPosition: \n", df.iloc[:,77])
# print(df.iloc[:, 60])       # 대표적인 null
# print(pd.isna(df.iloc[0, :]))
# print(df.isnull().sum())

''' 아무래도 null column이 2개 있는 것 같다. 어디인지 알아내자. '''

elist = [e for e in enumerate(df.iloc[0,:])]
for i in range(len(elist)):
    print(elist[i])

df.info()

# for i in range(102):
#     if str(df.iloc[0,i]) == "nan":
#         print(f"Find nan!! #{i}")
#     else:
#         continue

## 60, 61th col == "nan"

'''
## unusable key <input type='hidden' ... >
27	<class 'int'>	inhibitorTakedowns
50	<class 'int'>	nexusTakedowns                                  X
97	<class 'int'>	turretTakedowns

## Total usable: 102 / 105 (already applied)


## 내일 할일: 
1. df 내 column 재배치
2. match data 나열
    >> date, gameMode & Type, win, userLane, userstats, P2~P9 lane & stats
3. 피쳐 간 상관관계보기
'''


