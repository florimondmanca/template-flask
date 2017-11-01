# Flask application template

Minimal application template for Flask projects.

## Usage

### Using the template project

1. Make sure you've got [`cookiecutter`](http://cookiecutter.readthedocs.io/en/latest/installation.html) installed.

2. Cut the cookie:

```
$ cookiecutter https://github.com/florimondmanca/template-flask/
```

This will ask for a few details (name, email, project name, project short description, etc...).

3. `cd` to your newly generated project.

4. Create the virtual environment and install the dependencies (`$ pip install -r requirements.txt`).


### Running your application

For the sake of example, say you created `mysite` project called `mysite`.

Option 1 : use the `run.py` script located in `mysite`.

```
mysite $ python mysite/run.py
```

Option 2 : `mysite` contains a `__main__.py` file so you can run directly.

```
mysite $ python mysite
```


### Project structure

```
mysite
├── config.py
├── run.py
├── setup.py
└── mysite
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
