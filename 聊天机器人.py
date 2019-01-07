import json
import requests
while True:
    apikey = "5c959794b2a84795878fcf18f3d0ef38"
    url = "http://openapi.tuling123.com/openapi/api/v2"
    json_params ={
        "reqType":0,
        "perception": {
            "inputText": {
                "text": input("请输入您的问题")
            },
        },
        "userInfo": {
            "apiKey": apikey,  #换成自己的apikey
            "userId": "HHH"    #自定义名字
        }
    }
    content = requests.post(url,json=json_params).text
    # print(content)
    content = json.loads(content)
    result =  content.get('results')[0].get('values').get('text')
    print (result)
