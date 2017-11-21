import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "where":"nexearch",
    "sm":"top_sug.pre",
    "fbm":"0",
    "acr":"1",
    "acq":"chzhf",
    "qdt":"0",
    "ie":"utf8",
    "query":"초콜릿",
}

params = urllib.parse.urlencode(values)

# print(api)
# print(params)

url = api + "?" + params

print(url)

data = urllib.request.urlopen(url).read()
# print(data)

text = data.decode("utf-8") # or euc-something.
print(text)


# https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=chzhf&qdt=0&ie=utf8&query=초콜릿
# 方式：GET
# 対象：https://search.naver.com/ => ホスト名
# 追加情報
# - 経路： /search.naver
# - データ：
# ?where=nexearch
# &sm=top_sug.pre
# &fbm=0
# &acr=1
# &acq=chzhf
# &qdt=0
# &ie=utf8
# &query=초콜릿
