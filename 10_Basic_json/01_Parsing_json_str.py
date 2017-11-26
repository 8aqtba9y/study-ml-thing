# add modules
import urllib.request as request
import json

url = "https://api.github.com/repositories"

json_str = request.urlopen(url).read().decode('utf8')
output = json.loads(json_str)
# print(type(output), "- ", output)

for item in output:
    print("name:", item["name"])
    print("full_name:", item["full_name"])
    print("owner.login:", item["owner"]["login"])
    print()

# text = json.dumps(json_str)