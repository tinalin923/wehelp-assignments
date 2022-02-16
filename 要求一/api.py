from flask import Flask,request
from flask_restful import Api, Resource
from db import connection
app=Flask(__name__)
api=Api(app)   

class Members(Resource):    
    def get(self):
        u=request.args.get("username")
        query=("SELECT `id`,`name`,`username` FROM `member` WHERE `username`= %s")
        params=(u,)
        cursor= connection.cursor()
        cursor.execute(query,params)
        user=cursor.fetchone()
        cursor.close()
        if user == None:
            return{
                "data":user
            }
        else:
            id=user[0]
            name=user[1]
            username=user[2]     
            return {"data":{
                "id":id,
                "name":name,
                "username":username
            }}
    
api.add_resource(Members,"/api/members")  

if __name__ =="__main__":
    app.run(port="3000",debug=True)