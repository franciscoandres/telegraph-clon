from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

from app.telegraph.controllers import telegraph

app.register_blueprint(telegraph)

db.create_all()