# xmlの概要
#   xmlはインターネット上に提供されるデータ形式の一つである。
#   その他、json/csv/xlsなどがある。

# xmlの規則４つ
#   1. タグ:      <タグ></タグ>
#   2. コンテンツ: <タグ>{{コンテンツ}}</タグ>
#   3. 属性:      <タグ 属性="" 属性="" ... 属性=""></タグ>
#   4. ルートタグ: <?xml ?><ルートタグ/>

# add modules
from bs4 import BeautifulSoup
import urllib.request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()
# print(xml)
# <body>
#   <location wl_ver="3">
#   <province>서울ㆍ인천ㆍ경기도</province>
#   <city>서울</city>
#   <data>
#     <mode>A02</mode>
#     <tmEf>2017-11-27 00:00</tmEf>
#     <wf>구름조금</wf>
#     <tmn>-4</tmn>
#     <tmx>7</tmx>
#     <reliability>보통</reliability>
#   </data>

soup = BeautifulSoup(xml, "html.parser") # xml.parserとhtml.parserの差はない
seoul = soup.find_all("location")[0]
# print(seoul)

datas = seoul.find_all("data")
for data in datas:
    wf = data.find("wf")
    print(wf.text)