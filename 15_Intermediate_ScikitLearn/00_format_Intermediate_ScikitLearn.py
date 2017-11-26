from sklearn import model_selection, svm, metrics
import pandas

# format
#   train_data, test_data, train_label, test_label
#   clf = svm.SVC()
#   clf.fit(train_data, train_label)
#   prediction = clf.predict(test_data)
#   score = metrics.accuracy_score(test_label, prediction)
#   print("正答率: ",score)

train_csv = pandas.read_csv("./mnist/train.csv", header=None)
tk_csv = pandas.read_csv("./mnist/t10k.csv", header=None)

def convertToFloat(l): # 0~1:Float
    output = []
    for i in l:
        output.append(float(l) / 256)
    return output

# train_csv_data = train_csv.iloc[:, 1:].values
# tk_csv_data = tk_csv.iloc[:, 1:].values
train_csv_data = list(map(convertToFloat, train_csv.iloc[:, 1:].values))
tk_csv_data = list(map(convertToFloat, tk_csv.iloc[:, 1:].values))

train_csv_label = train_csv[0].values
tk_csv_label = tk_csv[0].values

clf = svm.SVC()
clf.fit(train_csv_data, train_csv_label)
prediction = clf.predict(tk_csv_data)
score = metrics.accuracy_score(tk_csv_label, prediction)
print("正答率: ",score)