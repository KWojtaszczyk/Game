from flask import render_template, flash, redirect
from webapp import app, forms


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Player'}
    return render_template('index.html', title='Main Menu', user=user)


@app.route('/splayer', methods=['GET', 'POST'])
def sp():
    form = forms.SinglePlayerEntryForm()
    if form.validate_on_submit():
        flash('Entry requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('splayer.html', title='Single Player', form=form)


@app.route('/mplayer', methods=['GET', 'POST'])
def mp():
    form = forms.MultiPlayerEntryForm()
    if form.validate_on_submit():
        flash('Entry requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('mplayer.html', title='Multiplayer', form=form)
