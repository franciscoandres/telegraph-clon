from flask import Blueprint, render_template, request, redirect, url_for

import app.utils as utils

from app import db
from app.telegraph.forms import PostForm
from app.telegraph.model import Post

telegraph = Blueprint("telegraph", __name__)

@telegraph.route("/", methods = ["POST", "GET"])
def new_post():

	form = PostForm(request.form)

	if form.validate_on_submit():
		title   = form.title.data
		slug    = title.lower().strip().replace(" ", "-")
		author  = form.author.data
		content = form.content.data

		post = Post(title, slug, author, content)
		db.session.add(post)
		db.session.commit()

		return redirect(url_for("telegraph.get_post", slug = slug))

	return render_template("telegraph/new.html", form = form)

@telegraph.route("/<slug>/")
def get_post(slug):
	post = Post.query.filter_by(slug = slug).first_or_404()
	return render_template("telegraph/single.html", post = post)

@telegraph.route("/<slug>/edit/", methods = ["POST", "GET"])
def edit_post(slug):

	post = Post.query.filter_by(slug = slug).first_or_404()

	if request.method == "POST":
		post.title   = request.form["title"]
		post.author  = request.form["author"]
		post.content = request.form["content"]
		db.session.commit()
		return redirect(url_for("telegraph.get_post", slug = slug))

	return render_template("telegraph/edit.html", post = post)
