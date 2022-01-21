from flask import Flask,render_template,request,redirect,url_for

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
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))
    
@app.route("/member/",methods=["GET"])
def member():
    return render_template('member.html')

@app.route("/error/")
def error():
    mess=request.args.get("message", " ")
    return render_template("error.html",message=mess) 
    
if __name__=="__main__":     
    app.run(port="3000",debug=True)         