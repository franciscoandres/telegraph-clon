from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title   = StringField("title", validators=[DataRequired(message="Title field is required")])
    author  = StringField("author", validators=[DataRequired(message="Author field is required field")])
    content = StringField("content", widget=TextArea(), validators=[DataRequired(message="Content field is required field")])
