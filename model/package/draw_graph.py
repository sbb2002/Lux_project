import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, roc_auc_score

# For Model validation
### To use, just fill "y_train, y_scores" in.

def plot_pr_vs_threshold(y_train, y_scores):
    precisions, recalls, thresholds = precision_recall_curve(y_train, y_scores)
    f1_scores = np.true_divide(2, np.true_divide(1, precisions) + np.true_divide(1, recalls))
    precision_eq = precisions[np.argmin(np.abs(precisions-recalls))]
    recall_eq = recalls[np.argmin(np.abs(precisions-recalls))]
    threshold_eq = thresholds[np.argmin(np.abs(precisions-recalls))]
    print(f"Precision: {precision_eq} \
        \nRecall: {recall_eq} \
        \nThreshold: {threshold_eq}")
    plt.figure(figsize=(6,6))
    plt.plot(thresholds, precisions[:-1], "b--", label='Precision', linewidth=2)
    plt.plot(thresholds, recalls[:-1], "g--", label="Recall", linewidth=2)
    plt.plot(thresholds, f1_scores[:-1], "k--", label="f1 score", linewidth=2)
    plt.legend(loc='center right', fontsize=16)
    plt.xlabel("Threshold", fontsize=16)
    plt.grid(True)
    plt.axis([np.min(thresholds), np.max(thresholds), 0 ,1])
    plt.plot([threshold_eq, threshold_eq], [0, recall_eq], "k:")
    plt.plot([np.min(thresholds), threshold_eq], [recall_eq, recall_eq], "r:")
    plt.plot([threshold_eq], [recall_eq], "ro")
    plt.show()

    return threshold_eq
    
def plot_p_vs_r(y_train, y_scores):
    precisions, recalls, _ = precision_recall_curve(y_train, y_scores)
    precision_eq = precisions[np.argmin(np.abs(precisions-recalls))]
    recall_eq = recalls[np.argmin(np.abs(precisions-recalls))]
    plt.figure(figsize=(6,6))
    plt.plot(recalls, precisions, "b--", linewidth=2)
    plt.xlabel("Recall", fontsize=16)
    plt.ylabel("Precisions", fontsize=16)
    plt.axis([0,1,0,1])
    plt.grid(True)
    plt.plot([recall_eq, recall_eq], [precision_eq, precision_eq], "ro")
    plt.plot([recall_eq, recall_eq], [0, precision_eq], "r:", linewidth=2)
    plt.plot([0, recall_eq], [precision_eq, precision_eq], "r:", linewidth=2)
    plt.show()

def plot_roc_curve(y_train, y_scores, label=None):
    fpr, tpr, _ = roc_curve(y_train, y_scores)
    auc = roc_auc_score(y_train, y_scores)

    fpr_eq = fpr[np.argmax(np.abs(fpr-tpr))]
    tpr_eq = tpr[np.argmax(np.abs(fpr-tpr))]
    print(f"AUC score: {auc}")
    plt.figure(figsize=(6,6))
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0,1],[0,1],'k--')
    plt.axis([0,1,0,1])
    plt.xlabel("FP rate", fontsize=16)
    plt.ylabel("TP rate", fontsize=16)
    plt.grid(True)
    plt.plot([fpr_eq], [tpr_eq], "ro")
    plt.plot([fpr_eq, fpr_eq], [0, tpr_eq], "r:")
    plt.plot([0, fpr_eq], [tpr_eq, tpr_eq], "r:")
    plt.plot()
    plt.show()

# For showing histogram
def lane2hist(df, lane):
    tempset1 = df.iloc[:, 3:8]
    tempset2 = df.iloc[:, 10:15]
    newset = pd.DataFrame(columns=['name', 'lane'])

    length = df.shape[0]
    for idx in range(length):
        for i in range(5):
            name1 = tempset1.iloc[idx, i].split(',')[0].strip()
            name2 = tempset2.iloc[idx, i].split(',')[0].strip()
            lane1 = tempset1.iloc[idx, i].split(',')[1].strip()
            lane2 = tempset2.iloc[idx, i].split(',')[1].strip()
            new1 = pd.Series([name1, lane1], index=['name', 'lane'])
            new2 = pd.Series([name2, lane2], index=['name', 'lane'])
 
            if lane == lane1:
                newset = newset.append(new1, ignore_index=True)
            elif lane == lane2:
                newset = newset.append(new2, ignore_index=True)

    x = newset['name'].value_counts().sort_index(ascending=True).keys()
    y = newset['name'].value_counts().sort_index(ascending=True)


    plt.figure(figsize=(50, 15))
    plt.xticks(rotation=45, fontsize=15)
    plt.yticks(fontsize=35)
    plt.ylabel('Pick counts', fontsize=35)
    plt.bar(x, y)
    plt.bar(x[np.argsort(-y)[0]], y[np.argsort(-y)[0]], color='#FF0000')
    plt.bar(x[np.argsort(-y)[1:5]], y[np.argsort(-y)[1:5]], color='#FFA600')
    plt.bar(x[np.argsort(-y)[5:10]], y[np.argsort(-y)[5:10]], color='#32D106')
    plt.bar(x[np.argsort(-y)[10:20]], y[np.argsort(-y)[10:20]], color='#06B5D1')
    plt.text(x[np.argmax(y)], y[np.argmax(y)], y[np.argmax(y)], fontsize=20, color='#FF0000', horizontalalignment='center', verticalalignment='bottom')
    plt.show()
    plt.close()
    return newset.value_counts().head(10)