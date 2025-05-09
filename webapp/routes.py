from flask import render_template
from webapp import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Player'}
    return render_template('index.html', title='Main Menu', user=user)
