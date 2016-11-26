from flask import Blueprint, render_template

telegraph = Blueprint("telegraph", __name__)

@telegraph.route("/")
def index():
	return render_template("telegraph/index.html")