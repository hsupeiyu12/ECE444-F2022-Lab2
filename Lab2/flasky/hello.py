
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_moment import Moment

app = Flask(__name__)


from datetime import datetime
@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',current_time=datetime.utcnow())
    
moment = Moment(app)
bootstrap = Bootstrap(app)

"""

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


from flask_moment import Moment
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap

#4.1
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

#4.2
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    def validate_email(form, field):
        if "@" not in field.data:
            raise ValidationError('Please include an @ in the email address.')
        if "utoronto" not in field.data:
            raise ValidationError('Please use a UofT email address.')

#4.4
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
           flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))
