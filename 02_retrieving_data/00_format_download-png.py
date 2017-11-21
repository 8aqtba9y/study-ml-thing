import urllib.request

url = "https://i.vimeocdn.com/portrait/58832_300x300"
savename = "test.png"

mem = urllib.request.urlopen(url).read()

# as binary
with open(savename, mode="wb") as f:
    f.write(mem)
    print("saved!")

url = "http://api.aoikujira.com/ip/ini"

mem = urllib.request.urlopen(url).read()

# as text
print(mem.decode("utf-8"))