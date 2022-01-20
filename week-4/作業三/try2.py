from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(
    __name__,
    template_folder="./templates",
    static_folder="./static",
    static_url_path="/")  
    
app.secret_key=123654789

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
        return redirect(url_for("please",message="請輸入帳號、密碼"))   #在此輸入message="請輸入帳號、密碼"，才出現在網址上
    else:
        return redirect(url_for("wrong",message="帳號、或密碼輸入錯誤"))
    
@app.route("/member/",methods=["GET"])
def member():
    return render_template('member.html')

@app.route("/error/")          #會出現網址的quert string和頁面不同步
def wrong():
    mess="帳號、或密碼輸入錯誤"
    return render_template("error.html",message=mess)   

@app.route("/erro/")
def please():
    messa="請輸入帳號、密碼"
    return render_template("error.html",message=messa)  #在此輸入message="請輸入帳號、密碼"，才出現在頁面上
@app.route("/signout") 
def signout():
    return redirect(url_for("home"))




if __name__=="__main__":   
    app.run(port="3000",debug=True)               