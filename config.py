import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
CSRF_SESSION_KEY = "secretcsrfhere"

SECRET_KEY = "secretkeyhere"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = True