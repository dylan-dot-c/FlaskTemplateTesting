from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    content = TextAreaField('Content', validators=[InputRequired()])
    submit = SubmitField('Submit')