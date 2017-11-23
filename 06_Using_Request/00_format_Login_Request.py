import requests

session = requests.session()
url = "https://www.google.co.jp"

# パラメータ
data = {
    "a":"10",
    "b":"20"
}

# リクエスト方式(;get,post,put,deleteなど)
response = session.get(url, data=data)
response.raise_for_status()

print(response.text)