import requests

Base="http://127.0.0.1:3000/"    #put the url of "Running on"
response= requests.post(Base+"api/members")  # requests.get(url)
print(response.json())  # ".json" make this look like information ,not response object 
                        # JSON序列化(serializable): 最好將所有回傳的物件轉為json格式的字串