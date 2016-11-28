from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title   = StringField("title", validators=[DataRequired(message="Title field is required")])
    author  = StringField("author", validators=[DataRequired(message="Author field is required")])
    content = TextAreaField("content", validators=[DataRequired(message="Content field is required")])
