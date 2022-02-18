from flask import Blueprint,render_template,request,session,redirect,url_for
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
            return redirect(url_for("login_name.member"))

@login_bp.route('/member/')
def member():
    if "name" in session:
        name=session["name"]
        return render_template('member.html', name=name)
    else:
        return redirect(url_for("home_name.home"))

@login_bp.route('/error/')
def error():
    mess=request.args.get("message","")
    return render_template('error.html',message=mess)

@login_bp.route('/signout',methods=["GET"]) 
def signout():
    session.pop('name', None)     
    return redirect(url_for("home_name.home"))



@login_bp.route('/api/members',methods=["GET"])  
def search():
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
            "data":user
        }
    else:
        name=user[0]
        return {
            "data":{
                "name":name,
                "username":u
            }
        }