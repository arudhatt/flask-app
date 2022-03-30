from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


class SettingsForm(FlaskForm):
    premises_full = RadioField(label='Premises Full', choices=[('True', 'True'), ('False', 'False')])
    waitlist = RadioField(label='Waitlist Enabled', choices=[('True', 'True'), ('False', 'False')])
    submit = SubmitField('Submit')
