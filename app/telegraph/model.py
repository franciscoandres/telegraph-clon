from app import db

class Post(db.Model):

	__tablename__ = "post"

	id        = db.Column(db.Integer, primary_key = True)
	title     = db.Column(db.String(256), nullable = False)
	author    = db.Column(db.String(128), nullable = False)
	create_at = db.Column(db.DateTime(), default = db.func.current_timestamp())
	content   = db.Column(db.Text())

	def __init__(self, title, author, content):
		self.title   = title
		self.author  = author
		self.content = content

	def __repr__(self):
		return "<Post {}>".format(self.title)