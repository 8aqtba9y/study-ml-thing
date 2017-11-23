import requests
from bs4 import BeautifulSoup

# セッションの生成
session = requests.session()

# ログイン
url = "http://mtv.clinks.jp/?controller=login&action=login"
data = { # from Form Data
    "login.x": "39", # <someValue>
    "login.y": "12", # <someValue>
    "accountName": "<ID>", # <ID>
    "password": "<PW>" # <PW>
}

response = session.post(url, data=data) # post方式
response.raise_for_status()
# print(response.text)

soupHome = BeautifulSoup(response.text, "html.parser")
name = soupHome.select_one("#profile-nav > div.menuBody > div.data > div.item.name > a")
print("name: ", name.string)

# 登録時間を取得
url = "http://mtv.clinks.jp/?controller=blog&action=top"
response = session.get(url)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
regTime = soup.select_one("div.regTime")
print("regTime: ", regTime.string)

# ログインが可能になれば、アクセスできる情報が増える
# ログインする方法を簡単にまとめると、
#  1. 開発者ツールを用いて、どこでログインの処理が行われているのかを確認する
#  2. その際、どこに（;php）何で（;方式）リクエストをするのかを確認する
#  3. pythonで上記(;1., 2.)を実装する
#    3-1. requestモヂュールでsessionを生成する
#    3-2. sessionにリクエストの方式を選択する
#    3-3. raise_for_status関数でログイン処理を行う
