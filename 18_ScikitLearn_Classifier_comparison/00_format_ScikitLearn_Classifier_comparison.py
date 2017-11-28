# http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


files = glob.glob("./train/*.txt")
train_label = []
train_data = []
for file_name in files:
    # label取得
    basename = os.path.basename(file_name)
    lang = basename.split("-")[0]

    # テキスト取得
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    text = text.lower()
    file.close()

    # alphabet出現頻度取得
    code_a = ord("a")
    code_z = ord("z")
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1

    # 正規化(normalize;0~1)
    total_train = sum(count)
    count = list(
        map(lambda n: float(n)/total_train, count)
    )

    # リストに追加
    train_label.append(lang)
    train_data.append(count)


files = glob.glob("./test/*.txt")
test_label = []
test_data = []
for file_name in files:
    # label取得
    basename = os.path.basename(file_name)
    lang = basename.split("-")[0]

    # テキスト取得
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    text = text.lower()
    file.close()

    # alphabet出現頻度取得
    code_a = ord("a")
    code_z = ord("z")
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1

    # 正規化(normalize;0~1)
    total_test = sum(count)
    count = list(
        map(lambda n: float(n)/total_test, count)
    )

    # リストに追加
    test_label.append(lang)
    test_data.append(count)


names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

# グラフ準備 --- (1)
graph_dict = {}
score_list = []

# iterate over classifiers
for name, clf in zip(names, classifiers):
    # 学習 --- (2)
    clf.fit(train_data, train_label)

    # 証明 --- (3)
    prediction = clf.predict(test_data)
    score = metrics.accuracy_score(test_label, prediction)
    print("[Classifier: ",name,"], [正答率: ",score,"]")

    # リストに追加
    score_list.append(score)


graph_dict["score"] = score_list
print(graph_dict) # {'score': [1.0, 0.875, 0.875, 1.0, 0.875, 0.875, 0.375, 0.75, 0.75, 0.375]}

asclist = names
df = pd.DataFrame(graph_dict, index=asclist)

# グラフ描画 --- (2)
plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0, 1.0))
plt.savefig("00_result.png")

    # 可視化 --- (4)
# report = metrics.classification_report(test_label, prediction)
# print("--- report ---")
# print(report)