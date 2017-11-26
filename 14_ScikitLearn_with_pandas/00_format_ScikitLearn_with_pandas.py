# import modules
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# url = "https://github.com/pandas-dev/pandas/blob/master/pandas/tests/data/iris.csv"
# csv = pd.read_csv("00_iris.csv")
csv = pd.read_csv("00_iris_raw.csv") # - (1)企画

labels = csv["Name"]
# print(labels)

datas = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
# print(datas)

# train_test_split関数を用いて、learningデータとtestingデータを分ける
# paramで全てのデータセットを渡す
# returnでtrain_data, test_data, train_label, test_labelを返す
train_data, test_data, train_label, test_label =\
    train_test_split(datas, labels)

clf = svm.SVC()
clf.fit(train_data, train_label) # - (2)開発

prediction = clf.predict(test_data)
print(prediction)
score = metrics.accuracy_score(prediction, test_label) # - (3)証明
print("正答率: ", score)
