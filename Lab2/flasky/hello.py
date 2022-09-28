from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    
bootstrap = Bootstrap(app)

"""
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
"""

"""
from datetime import datetime
@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())
"""
