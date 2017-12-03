import codecs
import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()

# https://ithub.korean.go.kr/user/total/database/corpusManager.do
# filename = "toji.txt"
# file = codecs.open(filename, mode="r", encoding="utf-16")
# soup = BeautifulSoup(file, "html.parser")
soup = BeautifulSoup(xml, "html.parser")
body = soup.select_one("body")
text = body.getText()

twitter = Twitter()
word_dic = {}
lines = text.split("\r\n")
for line in lines:
    malist = twitter.pos(line)
    for taeso, pumsa in malist:
        if pumsa == "Noun":
            if not (taeso in word_dic):
                word_dic[taeso] = 0
            word_dic[taeso] += 1

keys = sorted(word_dic.items(),
              key=lambda  x:x[1],
              reverse=True)
for word, count in keys[:50]: # 50個まで出力
    print("{0}({1}) ".format(word, count), end="")
print()