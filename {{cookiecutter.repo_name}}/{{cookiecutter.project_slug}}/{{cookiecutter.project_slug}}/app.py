"""App and db factory module."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

from . import views  # noqa

db = SQLAlchemy(app)
