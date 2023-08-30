from flask import Flask

def CreateApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randommodnar fgkjldfhky^jhb$'
    #import routes
    from .routes import routes
    from .login import login
    app.register_blueprint(routes, url_prefix = '/')
    app.register_blueprint(login, url_prefix = '/') 
    return app

