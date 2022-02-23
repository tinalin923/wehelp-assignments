from flask import Blueprint,url_for,redirect,request
register_bp=Blueprint('register_name',__name__,template_folder='./templates',static_folder="./static")
from db import connection
 
@register_bp.route("/signup",methods=['POST'])
def signup():
    n= request.form["name"]
    u= request.form["username"]
    p= request.form["password"]
    
    if not n or not u or not p:
        return redirect(url_for("login_name.error",message="請輸入姓名、帳號或密碼"))
    
    else:
        cursor=connection.cursor() 
        query=(
            "INSERT INTO `member` (`name`, `username`, `password` )"
            "VALUES ( %s, %s, %s)"
            "ON DUPLICATE KEY "
            "UPDATE `username` = VALUES (username)"
            )
        params=(n,u,p)
        cursor.execute(query,params)
        connection.commit()
        new_id=cursor.lastrowid
        
        if  new_id != 0:
            cursor.close()
            
            return redirect(url_for("home_name.home"))            
        else:
            return redirect(url_for("login_name.error",message="帳號已經被註冊"))
    
    

   