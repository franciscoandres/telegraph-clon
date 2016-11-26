from flask import Flask 
from app.telegraph.controllers import telegraph

app = Flask(__name__)

app.config.from_object("config")

app.register_blueprint(telegraph)