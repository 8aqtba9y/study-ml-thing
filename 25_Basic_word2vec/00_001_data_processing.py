import codecs
import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()

# https://ithub.korean.go.kr/user/total/database/corpusManager.do
# fp = codecs.open("toji.txt", "r", encoding="utf-16")
# soup = BeautifulSoup(fp, "html.parser")
soup = BeautifulSoup(xml, "html.parser")
body = soup.select_one("body")
text = body.getText()

# data processing(;morpheme analysis) --- (1)
twitter = Twitter()
lines = text.split("\r\n")
results = []
for line in lines:
    r = []
    malist = twitter.pos(line, norm=True, stem=True)
    for (word, pumsa) in malist:
        if not pumsa in ["Josa","Eomi","Punctuation"]:
            r.append(word)
    results.append(
        (" ".join(r)).strip()
    )

output = (
    " ".join(results).strip()
)
print(output)

# ファイルに出力  --- (2)
wakati_file = 'toji.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
