from flask import Flask,render_template,url_for,request,redirect

app=Flask(__name__,template_folder='./templates',static_folder='./templates')  


@app.route("/",methods=["POST","GET"])
def home():
    return render_template('4v1.html',account=request.values['account'],password=request.value['password'])
    
    if request.method == "POST":
        
        if request.values['send']=='登入':
            return redirect("/member/")
            
    elif :
        return redirect("/error/?message=請輸入帳號、密碼")
    else :
        return redirect("/error/?message=輸入錯誤")


# @app.route("/signin",methods=["POST","GET"]) 
# def sign():
#     if request.method == "POST":
#         if request.values['send']=='登入':
#             return redirect(url_for('home'))
    
@app.route("/member/")
def mem():
    return render_template('member.html')

@app.route("/error/?message=請輸入帳號、密碼")
def please():
    return render_template('please.html')

@app.route("/error/?message=輸入錯誤")
def wrong():
    return render_template('wrong.html')

if __name__=="__main__":      #  如果以主程式執行
    app.run(port="3000",debug=True)               # 立刻啟動伺服器