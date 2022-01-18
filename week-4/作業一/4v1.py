from flask import Flask,render_template,url_for

app=Flask(__name__,template_folder='./templates',static_folder='./templates')  

@app.route("/")
def home():
     return render_template('4v1.html')
    
if __name__=="__main__":     
    app.run(port="3000")             