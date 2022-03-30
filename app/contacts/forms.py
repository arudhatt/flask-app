from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class VisitorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email Id', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')