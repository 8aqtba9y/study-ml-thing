import urllib.request
import urllib.parse

# this api occurs error.
# urllib.error.HTTPError: HTTP Error 416: Requested Range Not Satisfiable
api = "https://www.homes.co.jp/chintai/tokyo/line/price/"
# values = {}

# params = urllib.parse.urlencode(values)

url = api # + "?" + params
print(url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8") # or euc-jp something.

# https://www.homes.co.jp/chintai/tokyo/line/price/
# 方式：GET? POST?
# 対象：https://www.homes.co.jp
# 追加情報
# - 経路：/chintai/tokyo/line/price/
# - データ：なし
