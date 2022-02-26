from flask import Flask

from home.views import home_bp
from login.views import login_bp
from register.views import register_bp


def create_app():    
    app=Flask(__name__)                                      
    app.config.from_object('config.DevConfig')   
                                                 
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)        
    app.register_blueprint(register_bp)     
   
    
    return app
    
if __name__=="__main__":     
     
    create_app().run(port="3000")         