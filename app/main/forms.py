from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditProfileFrom(FlaskForm):
    name = StringField('Real name', validators = [Length(0,64)])
    location = StringField('Location', validators = [Length(0,64)])
    about_me = TextAreaField('Aboute me')
    submit = SubmitField('Submit')




