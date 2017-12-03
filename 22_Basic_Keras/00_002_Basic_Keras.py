# moduleを読み込む --- (1)
# データを加工する --- (2)
# モデルを生成する --- (3)
# 学習させる --- (4)
# 予測させる --- (5)
# 正答率を確認する --- (6)

# (1) --- moduleを読み込む
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np


# (2) --- データを加工する
# 以下のデータをnumpy配列に変換する
# [
#     [<身長>, <体重>],   # 0.0 ~ 1.0
#     [<身長>, <体重>],   # 0.0 ~ 1.0
#     [<身長>, <体重>]    # 0.0 ~ 1.0
# ]
#
# [
#     "thin",     # [1, 0, 0]
#     "normal",   # [0, 1, 0]
#     "fat"       # [0, 0, 1]
# ]
csv = pd.read_csv("00_bmi.csv")
csv["weight"] /= 200
csv["height"] /= 100

bmi_class = {
    "thin": [1,0,0],
    "normal": [0,1,0],
    "fat": [0,0,1]
}
y = np.empty((20000,3)) # deep learningでは dataを x, labelを yという
# [
#     [0,0,0] 1行目
#     [0,0,0] 2行目
#     ...
#     [0,0,0] 20000行目
# ]

for index, value in enumerate(csv["label"]):
    y[index] = bmi_class[value]

x = csv[["weight","height"]].as_matrix()
x_train, y_train = x[1:15001], y[1:15001]
x_test, y_test = x[15001:20001], y[15001:20001]


# (3) --- モデルを生成する
model = Sequential()

# レイヤー生成
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))

# https://keras.io/optimizers/
# https://keras.io/losses/
model.compile(
    optimizer="rmsprop",
    loss="categorical_crossentropy",
    metrics=['accuracy']
)


# (4) --- 学習させる
model.fit(x_train, y_train)
          # batch_size=100,   # default=30
          # nb_epoch=20,      # default=1
          # validation_split=0.1,
          # callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
          # verbose=1)

# (5) --- 予測させて、model.predict()
# (6) --- 正答率を確認する
score = model.evaluate(x_test, y_test)
loss = score[0]
accuracy = score[1]
print("score loss: ", loss)
print("score accuracy: ", accuracy)