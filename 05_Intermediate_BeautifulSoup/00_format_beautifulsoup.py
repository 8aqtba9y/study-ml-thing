import urllib.request # get response with url by using urlopen({$url})
from bs4 import BeautifulSoup # create soup with response and parser type by using bs constructor

url = "http://info.finance.naver.com/marketindex/?tabSel=exchange"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("span.value")
for rs in results :
    print(rs)
# <span class="value">1,093.00</span>
# <span class="value">971.77</span>
# <span class="value">1,282.91</span>
# <span class="value">164.65</span>
# <span class="value">112.2100</span>
# <span class="value">1.1738</span>
# <span class="value">1.3258</span>
# <span class="value">93.9900</span>
# <span class="value">56.09</span>
# <span class="value">1526.88</span>
# <span class="value">1274.6</span>
# <span class="value">44983.4</span>

print("USD: ", results[0].string) # USD:  1,093.00
print("JPY: ", results[1].string) # JPY:  971.77
print("EUR: ", results[2].string) # EUR:  1,282.91
