import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('data/csv/KR_5138516254.csv', encoding='utf-8', delimiter=',')

# elist = [e for e in enumerate(df.iloc[0,:])]
# for i in range(len(elist)):
#     print(elist[i])

print(df.head(10))

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

print(df.corr(method='pearson'))