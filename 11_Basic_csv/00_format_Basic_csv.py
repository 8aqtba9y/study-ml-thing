# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
csv = """
p,x,s,n,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,y,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,n,n,g
e,b,s,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,m
p,x,y,w,t,p,f,c,n,n,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,g,f,n,f,w,b,k,t,e,s,s,w,w,p,w,o,e,n,a,g
"""

splitted = csv.split()
for item in splitted:
    list_mushroom = item.split(sep=",")
    print(list_mushroom)

    # 要素選択
    # print(list_mushroom[0]) # 1番目のelement
    # print(list_mushroom[1]) # 2番目のelement
    # print(list_mushroom[-2]) # 後ろから、2番目のelement
    # print(list_mushroom[-1]) # 後ろから、1番目のelement

    # 範囲選択
    # print(list_mushroom[1:4]) # 2番目のelementから、4番目のelementまで
    # print(list_mushroom[5:10]) # 6番目のelementから、10番目のelementまで
    # print(list_mushroom[:10]) # 最初のelementから、10番目のelementまで
    # print(list_mushroom[5:]) # 6番目のelementから、最後のelementまで