# add modules
import urllib.request
from bs4 import BeautifulSoup
import time

# listing article title
url = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#section_body a")

# listing article
for rs in results:
    print("title: ", rs.attrs["title"])
    article_url = rs.attrs["href"]

    response = urllib.request.urlopen(article_url)
    soup_article = BeautifulSoup(response, "html.parser")
    article = soup_article.select_one("#articleBodyContents")
    # print("body: ", article.string) # .string gives you text in 'TAG'
    # print("body: ", article.contents) # .contents gives you TAG instance

    # 加工する（pythonの文字列処理領域）
    # tip : 特徵抽出
    output = ""

    for item in article.contents:
        stripped = str(item).strip()
        if stripped == "": # is empty string?
            continue
        if stripped[0] not in ["<", "/"]: # isn't tag or comment?
            output += str(item).strip()

    print("body: ", output.replace("본문 내용TV플레이어", ""))

    # sleep 1 sec
    time.sleep(1) # サーバに短時間内に何度もアクセスしてはいけない
