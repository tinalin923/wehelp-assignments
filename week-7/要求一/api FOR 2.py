from flask import Flask,request
from flask_restful import Api, Resource
from db import connection
app=Flask(__name__)
api=Api(app)   

class Members(Resource):    
    def get(self):
        u=request.args.get("username")
        cursor=connection.cursor()
        query=(
            "SELECT `name` FROM `member` WHERE `username`=%s"
            )
        params=(u,)
        cursor.execute(query,params)
        user= cursor.fetchone()
        cursor.close()
        if user==None:
            return {
                "data":"無此帳號"
            }
        else:
            name=user[0]
            return { "data":{
                    'name':name,
                    'username':u}
                }
            
api.add_resource(Members,"/api/members")  

if __name__ =="__main__":
    app.run(port="3000",debug=True)