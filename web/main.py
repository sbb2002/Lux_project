from numpy.core.numeric import cross
import pandas as pd
import os, pickle
from package import data_preprocessing
from package import dev_lol, addheader
from flask import Flask, request, render_template, redirect
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_score

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def mainpage():
    return render_template("main.html")

@app.route("/prediction")
def data():
    # Prepare user's dataset.
    summonerName = request.args.get("summonerName")
    champion = request.args.get("champion")
    lane = request.args.get("lane")
    if lane == None:
        lane_str = "all"
    else:
        lane_str = lane

    tier = dev_lol.getTier(summonerName)
    if tier == "DIAMOND":
        tier_range = ["DIAMOND-I", "DIAMOND-II", "DIAMOND-III", "DIAMOND-IV"]
    elif tier == "PLATINUM":
        tier_range = ["PLATINUM-I", "PLATINUM-II", "PLATINUM-III", "PLATINUM-IV"]
    elif tier == "GOLD":
        tier_range = ["GOLD-I", "GOLD-II", "GOLD-III", "GOLD-IV"]
    elif tier == "SILVER":
        tier_range = ["SILVER-I", "SILVER-II", "SILVER-III", "SILVER-IV"]
    elif tier == "BRONZE":
        tier_range = ["BRONZE-I", "BRONZE-II", "BRONZE-III", "BRONZE-IV"]
    else:
        tier_range = None

    puuid = dev_lol.getPuuid(summonerName)
    matchlist = dev_lol.getMatchlist(puuid)
    raw = dev_lol.getData(summonerName, matchlist)

    mydf_v1 = dev_lol.dataset_for_me(raw, champion, lane, tier_range)
    mydf_v1.drop(['rank'], axis=1, inplace=True)
    mydf = dev_lol.dataset_for_me_v2(raw, champion, lane, tier_range)
    mydf.drop(['rank'], axis=1, inplace=True)

    # Check that pkl file exists...
    if not os.path.exists(r'web\pkl\{}_{}_{}_v1.pkl'.format(champion, lane_str, tier_range)):
        print("There is no model. Create a model. Wait a minute.")
        # Training and saving model.
        xy = data_preprocessing.dataset(champion, lane, tier_range)
        X_train, X_test, y_train, y_test = data_preprocessing.tt_split(xy)
        lrg_v1 = LogisticRegression()
        lrg_v1.fit(X_train, y_train)
        data_preprocessing.save_model(f"{champion}_{lane_str}_{tier}_v1", lrg_v1)
        print("Save a model(v1) successfully!")
    else:
        with open(r'web\pkl\{}_{}_{}_v1.pkl'.format(champion, lane_str, tier), 'rb') as f:
            print("Found a model(v1).")
            lrg_v1 = pickle.load(f)        

    if not os.path.exists(r'web\pkl\{}_{}_{}_v2.pkl'.format(champion, lane_str, tier)):
        print("There is no model. Create a model. Wait a minute.")
        # Training and saving model.
        xy = data_preprocessing.dataset_v2(champion, lane, tier_range)
        X_train, X_test, y_train, y_test = data_preprocessing.tt_split(xy)
        lrg = LogisticRegression()
        lrg.fit(X_train, y_train)
        data_preprocessing.save_model(f"{champion}_{lane_str}_{tier}_v2", lrg)
        print("Save a model(v2) successfully!")
    else:
        with open(r'web\pkl\{}_{}_{}_v2.pkl'.format(champion, lane_str, tier), 'rb') as f:
            print("Found a model(v2).")
            lrg = pickle.load(f)
    
    # Predict and create html. (v1)
    x = mydf_v1.iloc[:, 2:-1]
    y = mydf_v1.iloc[:, [-1]]
    predictions = lrg_v1.predict(x)
    predictions_proba = lrg_v1.predict_proba(x)
    win_proba = ["{:.2f}%".format(e[1]*100) for e in predictions_proba]
    model_predict = pd.DataFrame(predictions, columns=['prediction'])
    model_proba = pd.DataFrame(win_proba, columns=['win_proba'])
    final_df = pd.concat([mydf_v1, model_predict, model_proba], axis=1)
    df_html_v1 = final_df.to_html(justify='center')

    # Predict and create html. (v2)
    x = mydf.iloc[:, 2:-1]
    y = mydf.iloc[:, [-1]]
    predictions = lrg.predict(x)
    predictions_proba = lrg.predict_proba(x)
    win_proba = ["{:.2f}%".format(e[1]*100) for e in predictions_proba]
    model_predict = pd.DataFrame(predictions, columns=['prediction'])
    model_proba = pd.DataFrame(win_proba, columns=['win_proba'])
    final_df = pd.concat([mydf, model_predict, model_proba], axis=1)
    df_html_v2 = final_df.to_html(justify='center')

    df_html = df_html_v1 + df_html_v2

    full_html = addheader.addhead(tier, df_html)
    with open(r'web\templates\temp\{}_{}.html'.format(summonerName, champion), 'w', encoding='utf-8') as f:
        f.write(full_html)

    return render_template(f"temp/{summonerName}_{champion}.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)


## dev_lol.tt_split()에서 minmaxscaler를 주석처리하여 사용하지 않았다.
## 그런데 사용했을 때보다 더 성능이 좋았다.
## 이 성능의 판단 기준은 mydf의 win column과 prediction column이 일치하는 경우의 갯수로 판단하였다.

## 이제 win, prediction, proba에 색을 입혀보자.
## 아니면 여기서 멈추어도 되겠다. 완성!

## StandardScaler, RobustScaler, MaxAbsScaler를 기존의 MinMaxSclaer를 대신해보았는데,
## 역시 모두 결과가 좋지않았다. 스케일러들이 오히려 과적합시키는 것 같다.
## 스케일러들을 사용하지 않는 것이 바람직하다.