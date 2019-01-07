#  接口   API       (网址)
#  接口数据格式   : xml(基本不存在) / json(普遍)
import requests
url = "http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?"
content = requests.get(url).text
# print(content)                 #数据格式是 json
# json 和字典的关系
# 如果把字典转换成字符串 就是 json
# 把json 转换        就是 字典
import json
#  #    json字符串 转  字典
tianqi = json.loads(content)
# print(tianqi)
# # 一层一层剥开她的心
today = tianqi.get("results")[0].get("weather_data")[0]
print(today)
print(f"当前的日期为{today.get('date')}")
print(f"当前的日期为{today.get('date')}")
pm = tianqi.get("results")[0]
print(pm)
print(f"当前的pm2.5为{pm.get('pm25')}")
print(f"当前的des为{pm.get('index')[0].get('des')}")
#  #    字典  转  json字符串
# 如果字典中有汉字,转换的时候可能会出现乱码,这需要设置  ensure_ascii=False
# json_Str = json.dumps(tianqi)
json_Str = json.dumps(tianqi,ensure_ascii=False)
# print(json_Str)