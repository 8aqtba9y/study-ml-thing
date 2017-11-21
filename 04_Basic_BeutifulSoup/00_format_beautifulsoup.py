from bs4 import BeautifulSoup

html="""
<html><body>
<div id="meigen">
  <h1>wiki books</h1>
  <ul class="items art it book">
    <li>unity game effect</li>
    <li>swift iphone app</li>
    <li>modern web site design</li>
  </ul>
</div>
</body></html>
"""

# BeautifulSoupインスタンスを生成し、soup変数に保存する。
# インスタンス生成時、パラメータ「html文字列」と「parserの種類」を渡す。
soup = BeautifulSoup(html, 'html.parser')

# 単一ターゲットの場合、
header = soup.select_one("body > div > h1")
# bodyの下のdivの下のhiの要素になる

# 複数ターゲットの場合、
list_items = soup.select("ul.items > li")
# 要素の配列になる

print(header.string)
# wiki books

print(soup.select_one("ul").attrs)
# {'class': ['items', 'art', 'it', 'book']}

for li in list_items:
    print(li.string)
# unity game effect
# swift iphone app
# modern web site design

# ログ：
# print(header)
# <h1>wiki books</h1>

# print(list_items)
# [
#  <li>unity game effect</li>
#  , <li>swift iphone app</li>
#  , <li>modern web site design</li>
# ]

# 補足：
# TAG選択子
# ”h1”
# "html"

# ID選択子
# <ID名>

# CLASS選択子
# <CLASS名>.<CLASS名>.<CLASS名>....<CLASS名>
# 例）items.art.it.book

# 子孫選択子
# "meigen li"

# 子供選択子
# "ul.items > li"
