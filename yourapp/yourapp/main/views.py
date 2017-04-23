from flask import render_template, redirect, url_for
from . import main
from .forms import EmailPasswordForm

# Define your views here


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():

        # Check the password and log the user in
        # [...]

        return redirect(url_for('.index'))
    return render_template('login.html', form=form)
