import urllib.request
import urllib.parse

# it works
api = "https://sumaity.com/chintai/tokyo/"
values = {
    "lid":"smt10008"
}

params = urllib.parse.urlencode(values)

url = api + "?" + params
print(url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8") # or euc-jp something.
print(text)

# https://sumaity.com/chintai/tokyo/?lid=smt10008
# 方式：GET? POST?
# 対象：https://sumaity.com
# 追加情報
# - 経路：/chintai/tokyo/
# - データ
#  ?lid=smt10008
