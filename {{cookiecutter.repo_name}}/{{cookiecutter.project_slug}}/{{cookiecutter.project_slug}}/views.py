"""Views for {{cookiecutter.project_slug}}."""

from flask import render_template, redirect, url_for, request
from .app import app
from .forms import EmailPasswordForm

# Define your views here


@app.route('/')
def index():
    """Example index view."""
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    """Example login form view."""
    form = EmailPasswordForm()
    if request.method == 'POST' and form.validate():
        # TODO Check the password and log the user in
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)
