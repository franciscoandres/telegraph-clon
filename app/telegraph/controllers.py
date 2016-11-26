from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.telegraph.model import Post

telegraph = Blueprint("telegraph", __name__)

@telegraph.route("/", methods = ["POST", "GET"])
def index():

	if request.method == "POST":
		title   = request.form["title"]
		slug    = title.lower().strip().replace(" ", "-")
		author  = request.form["author"]
		content = request.form["content"]

		post = Post(title, slug, author, content)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for("telegraph.get_post", slug = slug))

	return render_template("telegraph/index.html")

@telegraph.route("/<slug>")
def get_post(slug):
	
	post = Post.query.filter_by(slug = slug).first_or_404()
	return render_template("telegraph/post.html", post = post)