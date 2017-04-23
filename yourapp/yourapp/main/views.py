from flask import render_template
from . import main

# Define your views here


@main.route('/')
def index():
    return render_template('index.html')
