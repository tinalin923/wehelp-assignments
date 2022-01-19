from flask import Flask,render_template,request,redirect

app=Flask(
    __name__,
    template_folder="./templates",
    static_folder="./static",
    static_url_path="/")  

@app.route("/")      
def home():
    return render_template('4v1.html')
    
@app.route("/signin",methods=["POST"]) 
def sign():
    account= request.form["account"]
    password= request.form["password"]
    if account=="test" and password=="test":
        return redirect("/member/")
    if account=="" or password=="":
        return redirect("/error/?message=請輸入帳號、密碼")   #想直接導入該網址xd 失敗~
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")
    
@app.route("/member/",methods=["GET"])
def member():
    return render_template('member.html')

@app.route("/error/?message=請輸入帳號、密碼")
def please():
    return render_template("error.html",message="請輸入帳號、密碼")


@app.route("/error/?message=帳號、或密碼輸入錯誤")
def wrong():
    return render_template("error.html",message="帳號、或密碼輸入錯誤")



if __name__=="__main__":      #  如果以主程式執行
    app.run(port="3000",debug=True)               # 立刻啟動伺服器