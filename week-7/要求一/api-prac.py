from flask import Flask,jsonify
from flask_restful import Api, Resource,reqparse

app=Flask(__name__)
api=Api(app)    #wrap app in a api,and inintialize the fact that we're using a restfual api
parser=reqparse.RequestParser()

class helloWorld(Resource):    #Resource within the api
    def get(self):                  #使用 Get request 會回傳的回應
        return {"hello world":1}    #codes for handle the requests (what happen when a request is sent to specific url)
    def post(self):                 #使用 Post request 會回傳的回應
        return {"data":"posted"}

api.add_resource(helloWorld,"/api/members")  #register the api as a resource and set endpoint (the name of class,be accessible at specific url)
#第一個/代表default url,後面的api/members代表endpoint,只有當使用者輸入這個url時，才會觸發此resource

if __name__ =="__main__":
    app.run(port="3000",debug=True)