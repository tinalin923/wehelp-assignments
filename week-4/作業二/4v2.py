from flask import Flask,render_template,url_for,request

app=Flask(__name__)  


@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        if request.values['send']=='登入':
            return render_template('4v1.html',account=request.values['account'],password=request.value['password'])
    return render_template('4v1.html',account="",password="")


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