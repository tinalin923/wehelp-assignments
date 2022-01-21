from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(
    __name__,
    template_folder="./templates",
    static_folder="./static",
    static_url_path="/")  

app.secret_key="123654789"

@app.route("/")      
def home():
    return render_template('4v1.html')
    
@app.route("/signin",methods=["POST"]) 
def signin():
    account= request.form["account"]
    password= request.form["password"]
    
    if account=="test" and password=="test":
        session["account"]="test"
        session["password"]="test"
        return redirect("/member/")
    if account=="" or password=="":
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))
    
@app.route("/member/",methods=["GET"])
def member():
    if "account" in session and "password" in session:
        return render_template('member.html')
    else:
        return redirect(url_for("home"))
@app.route("/error/")
def error():
    mess=request.args.get("message","")
    return render_template("error.html",message=mess) 
    
@app.route("/signout",methods=["GET"]) 
def signout():
    session.pop('paccount', None)     
    session.pop('password', None)
    return redirect(url_for("home"))


if __name__=="__main__":     
    app.run(port="3000",debug=True)         