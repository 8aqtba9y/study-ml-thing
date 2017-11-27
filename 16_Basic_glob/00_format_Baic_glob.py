from sklearn import svm, metrics
import glob, os.path, re, json

files = glob.glob("./train/*.txt")
# print(files) # ['./train/en-1.txt','./train/en-2.txt','./train/en-3.txt',...'./train/tl-20.txt']

train_label = []
train_data = []
for file_name in files:
    # label取得
    basename = os.path.basename(file_name)
    lang = basename.split("-")[0]
    # print(basename, lang)
    # en-1.txt en
    # en-2.txt en
    # en-3.txt en
    # ...
    # tl-20.txt tl

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
            # 'a'97 - 'a'97 = 0
            # 'b'98 - 'a'97 = 1
            # ...
            count[code_current - code_a] += 1

    # 正規化(normalize;0~1)
    total_train = sum(count)
    count = list(
        map(lambda n: float(n)/total_train, count)
    ) # map関数のparams(param1:関数,param2:list)

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

# 学習 --- (2)
clf = svm.SVC()
clf.fit(train_data, train_label)

# 証明 --- (3)
prediction = clf.predict(test_data)
score = metrics.accuracy_score(test_label, prediction)
print("正答率: ",score)

# 可視化 --- (4)
report = metrics.classification_report(test_label, prediction)
print("--- report ---")
print(report)