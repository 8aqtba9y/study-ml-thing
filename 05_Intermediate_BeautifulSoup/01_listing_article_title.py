# import modules
import urllib.request
from bs4 import BeautifulSoup

# listing article title
url = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
# results = soup.select("strong")
# results = soup.select("#section_body strong")
results = soup.select("#section_body a") # '#section_body'の'#'はIDの選択子

for rs in results:
#     print(rs.string)
    print("title: ", rs.attrs["title"])
    print("link: ", rs.attrs["href"])
    print("")