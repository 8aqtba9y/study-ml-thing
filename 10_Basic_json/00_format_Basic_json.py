# JSON = オブジェクトを表現する方式の一つである
# 表現できるデータ型は６つある
#   1. 数字: 10 12.34
#   2. 文字列: "文字列" "0123456789"
#   3. BOOL: true false
#   4. null: null
#   5. 配列: [10, 12.34, "文字列", true]
#   6. オブジェクト: {
#                     "キーA": 10
#                     "キーB": "値"
#                     "キーA": true
#                     "キーA": ["文字列", 12.34]
#                   }

# add modules
import json

json_str = """[
    {"name": "りんご", "price": 1000},
    {"name": "バナナ", "price": 2000},
    {"name": "なし", "price": 3000},
    {"name": "みかん", "price": 4000}
]"""

# json文字列 => python Obj
output = json.loads(json_str)
print(type(output), "- ",output)
# <class 'list'> -  [{'price': 1000, 'name': 'りんご'}, {'price': 2000, 'name': 'バナナ'}, {'price': 3000, 'name': 'なし'}, {'price': 4000, 'name': 'みかん'}]

# python Obj => json文字列
text = json.dumps(output)
print(type(text), "- ",text)
# <class 'str'> -  [{"price": 1000, "name": "\u308a\u3093\u3054"}, {"price": 2000, "name": "\u30d0\u30ca\u30ca"}, {"price": 3000, "name": "\u306a\u3057"}, {"price": 4000, "name": "\u307f\u304b\u3093"}]

