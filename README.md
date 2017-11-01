# Flask application template

Minimal working application template for Flask projects.

## Usage

### Using the template project

1. Clone this repo in your project folder, e.g. `flaskproject`. Also rename the `flaskproject/yourapp` and `flaskproject/yourapp/yourapp` folders, for instance `flaskapp`.

2. Create the virtual environment and install the dependencies:
```
$ virtualenv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

3. Using your favorite text editor's find/replace functionality on the whole `flaskproject` directory with case sensitivity enabled, replace occurences of `yourapp` and `YOURAPP` with `flaskapp` and `FLASKAPP` respectively.

> Steps 2. and 3 will hopefully soon be automated.

### Running your application

```
flaskproject $ python3 flaskapp/run.py
```


## Contents

### Project structure

```
yourapp
├── config.py
├── run.py
├── setup.py
└── yourapp
    ├── __init__.py
    ├── app.py
    ├── views.py
    ├── models.py
    ├── forms.py
    ├── static
    │   └── css
    │       └── style.css
    └── templates
```

### Included extensions

This template project includes the following Flask extensions :

- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) for the database backend
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) for migrations.
- [Flask-WTForms](https://flask-wtf.readthedocs.io/en/stable/) for forms management.

### Included templates

The templates inside `yourapp/templates` include :

- a `base.html` template using Bootstrap 4 and declaring a few template blocks: `title`, `stylesheets`, `scripts`, `nav`, `content`
- an example `nav.html`
- two example view templates: `index.html`, `login.html`
- a `_form_helpers.html` file containing useful helpers for use with Flask-WTF


## References

This template project structure and contents was originally inspired by the [ExploreFlask](https://exploreflask.com/en/latest/) tutorials.
