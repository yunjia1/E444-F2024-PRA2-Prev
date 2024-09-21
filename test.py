
from flask import Flask

app = Flask(__name__)

#Activity 1.2
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

#Activity 1.3
# @app.route('/')
# def index():    
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

#Activity 1.4
# from flask_bootstrap import Bootstrap

# app = Flask(__name__)
# bootstrap = Bootstrap(app)

# @app.route('/')
# def index():    
#     return render_template('user.html', name="World")

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)