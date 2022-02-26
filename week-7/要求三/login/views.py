from getopt import gnu_getopt
from flask import Blueprint,render_template,request,session,redirect,url_for,jsonify,make_response
login_bp=Blueprint('login_name',__name__,template_folder='./templates',static_folder="./static")
from db import connection

@login_bp.route('/signin',methods=["POST"]) 
def signin():
    u= request.form["username"]
    p= request.form["password"]   
    if not u or not p:
        return redirect(url_for("login_name.error",message="請輸入帳號或密碼"))
    else:
        cursor=connection.cursor()
        query=(
            "SELECT `name`,`password` FROM `member` WHERE `username`=%s AND `password`=%s"
            )
        params=(u,p)
        cursor.execute(query,params)
        user= cursor.fetchone()
        cursor.close()
                
        if  user == None:
            return redirect(url_for("login_name.error",message="帳號或密碼輸入錯誤"))
        else:
            name=user[0] 
            session["name"]= name
            session["username"]=u
            session["password"]=p
            return redirect(url_for("login_name.member"))

@login_bp.route('/member/')
def member():
    if "name" in session:
        name=session["name"]
        return render_template('member.html', name_template=name)
    else:
        return redirect(url_for("home_name.home"))

@login_bp.route('/error/')
def error():
    mess=request.args.get("message","")
    return render_template('error.html',message=mess)

@login_bp.route('/signout',methods=["GET"]) 
def signout():
    session.clear()     
    return redirect(url_for("home_name.home"))


from flask import Blueprint,render_template,request,session,redirect,url_for,jsonify
api_bp=Blueprint('api_name',__name__,template_folder='./templates',static_folder="./static")
from db import connection

@api_bp.route('/api/members',methods=["GET"])  
def searchName():
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
        response=jsonify(
        {
            "data":user
        })
        return response
    else:
        name=user[0]
        response=jsonify(
        {
            "data":{
                "name":name,
                "username":u
            }
        })
        return response

@login_bp.route('/api/member',methods=['POST'])
def updateName():
    if "username" in session:      #要先在此確認會員有沒有登入
        req = request.get_json()   #取得前端傳過來的值    # 不要用new=request.form["newname"]
        new = req["name"]
        old = session["name"]
        u = session["username"]
        
        if new != old: 
            session.pop("name",None)
            session["name"]=new
            cursor=connection.cursor()
            query=(
                "UPDATE `member`"
                "SET `name`= %s"
                "WHERE `username`=%s"
            )
            params=(new,u)
            cursor.execute(query,params)
            connection.commit()
            cursor.close()
            response=make_response(jsonify({"ok":True}),200)
            # response=jsonify({"ok":True})
            return response
    else:
        response=jsonify({"error":True})
        return response
    # else:
    #     return redirect(url_for("login_name.member"))





