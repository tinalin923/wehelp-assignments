import urllib.request as request
import json

with request.urlopen ("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json") as response:
    data=json.load(response)
#print(data)

#要求:景點名稱,區域,經度,緯度,第一張圖檔網址
list=data["result"]["results"]
# print(list)
# for i in range(len(list)):    #len=58
#     web=list[i]["file"].lower()   #因為原始資料有大小寫的jpg，在find的時候會被視為不一樣的結果，所以要先統一
#     end=web.find("jpg")
#     print(list[i]["stitle"]+","+list[i]["address"][5:8]+","+list[i]["longitude"]+","+list[i]["latitude"]+","+web[0:end+3])

with open ("data.csv",mode="w",encoding="utf-8") as file:
    for i in range(len(list)):
        web=list[i]["file"].lower()   
        end=web.find("jpg")
        file.write(list[i]["stitle"]+","+list[i]["address"][5:8]+","+list[i]["longitude"]+","+list[i]["latitude"]+","+web[0:end+3]+"\n")


# str.lower()  字體變小寫
# end57=list[57]["file"].find("jpg")
# print(end57)  #回傳為-1 代表找不到jpg 因為資料是使用JPG!! 所以要先end57.lower()再.find("jpg")
# print(list[57]["file"].lower())


#print(list[0]["file"].find(".jpg"))
#end=list[0]["file"].find(".jpg")
#print(end)
#end+3  #所要找的第一個jpg的g的index




