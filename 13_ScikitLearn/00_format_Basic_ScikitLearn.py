# add modules
# `sklearn.svm` module includes Support Vector Machine algorithms
# `sklearn.metrics` module includes score functions, performance metrics
#   and pairwise metrics and distance computations.
from sklearn import svm, metrics

# xor - (1)企画
datas = [[0,0],[1,0],[0,1],[1,1]]
labels = [0, 1, 1, 0]
examples_datas = [[0,0],[1,0]]
examples_lables = [0,1]

# learning - (2)開発
clf = svm.SVC() # classifier => 機械学習のアルゴリズムを生成する
clf.fit(datas, labels) # first param: data ,second param: label

# test - (3)証明
prediction = clf.predict(examples_datas)
score = metrics.accuracy_score(examples_lables, prediction)
print("正答率: ", score)