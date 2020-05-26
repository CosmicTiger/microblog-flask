from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joker_LotusZero'}

    posts = [
        {
            'author': {'username': 'Juan'},
            'body': 'Beautiful Night in Nicaragua!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'CS50x.ni Is Cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)