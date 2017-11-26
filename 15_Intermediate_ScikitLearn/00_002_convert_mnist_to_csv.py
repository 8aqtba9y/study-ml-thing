import struct
def to_csv(name, maxdata):
    # labelファイルとimageファイルを開く
    lbl_f = open("./mnist/"+name+"-labels-idx1-ubyte", "rb") # read
    img_f = open("./mnist/"+name+"-images-idx3-ubyte", "rb") # read
    csv_f = open("./mnist/"+name+".csv", "w", encoding="utf-8")

    # ヘッダー情報を読み込む --- (1)
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", lbl_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols

    # imageデータをcsvデータに変換 --- (2)
    res = []
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(
                        lambda n:
                            str(n), bdata
                        )
                    )
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")

        # 正しく保存されたか検証するために、imageファイルとして保存 --- (3)
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name,idx,label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)

    csv_f.close()
    img_f.close()
    lbl_f.close()

# 結果をファイルに出力 --- (4)
to_csv("train", 1000)
to_csv("t10k", 500)

# csvファイルを確認 --- (5)
# input = "0 0 0 ... 0 0 0" # 28 * 28
# input = input.split(" ")
# for i in range(len(input)):
#     print("{:3}".format(input[i]),end=" ")
#     if i % 28 == 0:
#         print()