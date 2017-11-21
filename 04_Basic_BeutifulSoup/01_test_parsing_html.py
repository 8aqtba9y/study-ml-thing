import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# it works
api = "https://sumaity.com/chintai/tokyo/"
values = {
    "lid":"smt10008"
}

params = urllib.parse.urlencode(values)

url = api + "?" + params
print(url)

data = urllib.request.urlopen(url).read()
html = data.decode("utf-8") # or euc-jp something.
# print(html)

soup = BeautifulSoup(html, 'html.parser')

# 単一ターゲットの場合、
title = soup.select_one("head > title")
# headの下のtitleの要素になる

# 複数ターゲットの場合、
list_items = soup.select("tr.item > th")
# 要素の配列になる

print(title.string)
# 東京の賃貸(マンション・アパート)を探す【スマイティ】

print(soup.select_one("meta").attrs)
# {'http-equiv': 'Content-Type', 'content': 'text/html; charset=utf-8'}

for li in list_items:
    print(li.string)
# 駅名
# 市区郡
