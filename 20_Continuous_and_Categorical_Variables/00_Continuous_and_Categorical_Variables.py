# about fit and predict methods params

import urllib.request as req
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

local = "mushroom.data"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("ok")
# Mushroom Data Set Description
# https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names

# データを読み込む --- (1)
mr = pd.read_csv(local,header=None)

print("連続変数化")
# 文字データを数字に変換 --- (2)?Continuous variables
label = []
data = []
for row_index_ctn, row in mr.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(v))
    data.append(row_data)

print("label: ",label[0:2])
print("data: ",data[0:2])

# 学習データとテストデータに分ける --- (3)
data_train, data_test, label_train, label_test = train_test_split(data, label)

# 学習 --- (4)
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 証明 --- (5)
prediction = clf.predict(data_test)
score = metrics.accuracy_score(label_test, prediction)
print("正答率: ", score)

# 可視化 --- (6)
report = metrics.classification_report(label_test, prediction)
print("report:")
print(report)


print("分類変数化")
# 文字データを配列に変換 --- (2)?Categorical variables
label = []
data = []
attr_list = []
for row_index_ctg, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        if row_index_ctg == 0:
            attr = {"dic":{}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)


print("label: ",label[0:2])
print("data: ",data[0:2])

# 学習データとテストデータに分ける --- (3)
data_train, data_test, label_train, label_test = train_test_split(data, label)

# 学習 --- (4)
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 証明 --- (5)
prediction = clf.predict(data_test)
score = metrics.accuracy_score(label_test, prediction)
print("正答率: ", score)

# 可視化 --- (6)
report = metrics.classification_report(label_test, prediction)
print("report:")
print(report)


# TODO : cross validation