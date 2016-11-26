from flask import Blueprint, render_template, request

from app import db
from app.telegraph.model import Post

telegraph = Blueprint("telegraph", __name__)

@telegraph.route("/", methods = ["POST", "GET"])
def index():
	return render_template("telegraph/index.html")