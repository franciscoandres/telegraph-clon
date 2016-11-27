from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template("404.html"), 404

from app.telegraph.controllers import telegraph

app.register_blueprint(telegraph)

db.create_all()