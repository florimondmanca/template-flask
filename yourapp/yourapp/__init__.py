from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.register_blueprint(main)

db = SQLAlchemy(app)
