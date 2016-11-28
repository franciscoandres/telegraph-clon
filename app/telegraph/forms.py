from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title   = StringField("title", validators=[
        DataRequired(message="Title field is required"),
        Length(min = 3, max = 256, message = "Minimum 3 characters")
        ])
    author  = StringField("author", validators=[
        DataRequired(message="Author field is required"),
        Length(min = 3, max = 256, message = "Minimum 3 characters")
        ])
    content = TextAreaField("content", validators=[DataRequired(message="Content field is required")])
