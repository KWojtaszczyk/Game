from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SinglePlayerEntryForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    q_number = StringField('Number of questions', validators=[DataRequired()])
    submit = SubmitField('Enter the game')


class MultiPlayerEntryForm(FlaskForm):
    # need to figure out a way to show the appropriate number of fields for multiplayer
    username = StringField('Name', validators=[DataRequired()])
    q_number = StringField('Number of questions', validators=[DataRequired()])
    submit = SubmitField('Enter the game')
